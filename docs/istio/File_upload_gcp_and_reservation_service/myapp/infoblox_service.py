import json
import time
import requests
from requests.auth import HTTPBasicAuth
from bson import ObjectId, json_util
import logging
logger = logging.getLogger("django")

from myapp.permissions import Permission
from utils.mongo_utils import MongoQueryUtils

from utils.environment_configs import EnvironmentConfigs as env

mongo_utils = MongoQueryUtils()
network_collection = mongo_utils.get_collection_handle('networks')
reserved_ip_collection = mongo_utils.get_collection_handle(env.mongo_reserved_ips_collection)
users_collection = mongo_utils.get_collection_handle(env.mongo_users_collection)
audit_logs_collection = mongo_utils.get_collection_handle(env.mongo_audit_logs_collection)


class Infoblox_Service:
    def get_networks(self, request):
        permissionn = Permission().grant_user_permission(request.query_params['role']) or Permission().grant_admin_permission(request.query_params['role'])
        if permissionn:
            url = env.infoblox_url + '/network?_return_as_object=1'
            contents = requests.get(url, verify=False, auth=HTTPBasicAuth(env.infoblox_username, env.infoblox_password))
            jsondata = json.loads(contents.content)
            if 'Error' not in jsondata:
                jsondata['status'] = 200
            else:
                jsondata['status'] = 404
            logger.debug(jsondata)
            return jsondata
        else:
            jsondata = {"error": "Not authorised to process the request.", 'status': 403}
            logger.error(jsondata)
            return jsondata

    def get_ip_statuses(self, request):
        permissionn = Permission().grant_user_permission(request.query_params['role']) or Permission().grant_admin_permission(request.query_params['role'])
        if permissionn:
            url = env.infoblox_url + '/ipv4address?network=' + request.query_params[
                'network'] + '&_return_fields=status,ip_address,mac_address,network&_return_as_object=1'
            contents = requests.get(url, verify=False, auth=HTTPBasicAuth(env.infoblox_username, env.infoblox_password))
            jsondata = json.loads(contents.content)
            if 'Error' not in jsondata:
                jsondata['status'] = 200
                data_dict={}
                data_dict['_id'] = request.query_params['network']
                ip_list = []
                for data in jsondata['result']:
                    data['created_at'] = int(time.time())
                    ip_list.append(data)
                data_dict['ip'] = ip_list
                # network_collection.save(data_dict, check_keys=False)
            else:
                jsondata['status'] = 404
            logger.debug(jsondata)
            return jsondata
        else:
            jsondata = {"error": "Not authorised to process the request.", 'status': 403}
            logger.error(jsondata)
            return jsondata

    def reserve_ips(self, request):
        jsondata = {}
        result = []
        reserved_ip_success = []
        reserved_ip_failure = []
        audit_data = {}
        permissionn = Permission().grant_admin_permission(request.query_params['role'])
        if permissionn:
            url = env.infoblox_url + '/fixedaddress?_return_fields=ipv4addr,mac&_return_as_object=1'
            userdata = users_collection.find_one({'_id': ObjectId(request.data['userid'])})
            for ip in request.data['ip']:
                payload = '{  "ipv4addr":"' + ip + '",  "mac":"00:00:00:00:00:00"}'
                contents = requests.post(url, verify=False,
                                         auth=HTTPBasicAuth(env.infoblox_username, env.infoblox_password), data=payload)
                contents_jsondata = json.loads(contents.content)
                if 'Error' not in contents_jsondata:
                    contents_jsondata["result"]["username"] = userdata['username']
                    contents_jsondata["result"]["_id"] = contents_jsondata["result"]["ipv4addr"]
                    contents_jsondata["result"]["created_at"] = int(time.time())
                    reserved_ip_collection.save(contents_jsondata["result"], check_keys=False)
                    contents_jsondata["result"]['status'] = 201
                    result.append(contents_jsondata["result"])
                    reserved_ip_success.append(ip)
                else:
                    contents_jsondata['status'] = 404
                    result.append(contents_jsondata)
                    reserved_ip_failure.append(ip)
                logger.debug(jsondata)
            jsondata['result'] = result
            jsondata['reserved_ip_success'] = reserved_ip_success
            jsondata['reserved_ip_failure'] = reserved_ip_failure
            audit_data['reserved_ip_success'] = reserved_ip_success
            audit_data['reserved_ip_failure'] = reserved_ip_failure
            audit_data['created_at'] = int(time.time())
            audit_data["username"] = userdata['username']
            audit_logs_collection.save(audit_data, check_keys=False)
            if len(reserved_ip_success) > 0:
                jsondata['status'] = 201
            else:
                jsondata['status'] = 400
            return jsondata
        else:
            jsondata = {"error": "Not authorised to process the request.", 'status': 403}
            logger.error(jsondata)
            return jsondata

    def reserved_ips_list(self, request):
        permissionn = Permission().grant_admin_permission(request.query_params['role'])
        if permissionn:
            jsondata = {'reserved_ip_list': []}
            reserved_ip_cursor = reserved_ip_collection.find()
            for data in reserved_ip_cursor:
                jsondata['reserved_ip_list'].append(json.loads(json_util.dumps(data)))
            jsondata['status'] = 200
            return jsondata

        else:
            jsondata = {"error": "Not authorised to process the request.", 'status': 403}
            logger.error(jsondata)
            return jsondata

    def unreserve_ips(self, request):
            jsondata_list = []
            audit_data = {}
            unreserved_ip = []
            permissionn = Permission().grant_admin_permission(request.query_params['role'])
            if permissionn:
                jsondata = {}
                jsondata['ids'] = []
                userdata = users_collection.find_one({'_id': ObjectId(request.data['userid'])})
                for ip in request.data['ip']:
                    get_ref_url = env.infoblox_url + '/ipv4address?ip_address=' + ip
                    contents = requests.get(get_ref_url, verify=False,
                                            auth=HTTPBasicAuth(env.infoblox_username, env.infoblox_password))

                    contents_jsondata_ref = json.loads(contents.content)
                    reclaime_ip_url = env.infoblox_url + '/' + contents_jsondata_ref[0]['_ref']
                    reclaimed_jsondata = requests.delete(reclaime_ip_url, verify=False,
                                               auth=HTTPBasicAuth(env.infoblox_username, env.infoblox_password))
                    contents_jsondata = json.loads(reclaimed_jsondata.content)
                    jsondata['ids'].append(contents_jsondata)
                    reserved_ip_collection.delete_one({'ipv4addr': ip})
                    unreserved_ip.append(ip)
                logger.debug(jsondata_list)
                audit_data['unreserved_ip'] = unreserved_ip
                audit_data["username"] = userdata['username']
                audit_data['created_at'] = int(time.time())
                audit_logs_collection.save(audit_data, check_keys=False)
                jsondata['status'] = 200
                return jsondata
            else:
                jsondata = {"error": "Not authorised to process the request.", 'status': 403}
                logger.error(jsondata)
                return jsondata