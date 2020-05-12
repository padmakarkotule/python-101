import json
import logging

import time
from bson import ObjectId, json_util
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from myapp.file_handler_service import file_handler_service, bucket_handler_service
from myapp.infoblox_service import Infoblox_Service
from myapp.permissions import Permission
from myapp.searializers import RolesSerializer, UsersSerializer, FileSerializer
from utils.environment_configs import EnvironmentConfigs as env
from utils.mongo_utils import MongoQueryUtils
from google.cloud import storage

logger = logging.getLogger("django")

mongo_utils = MongoQueryUtils()
role_collection = mongo_utils.get_collection_handle(env.mongo_roles_collection)
users_collection = mongo_utils.get_collection_handle(env.mongo_users_collection)

@csrf_exempt
@api_view(['GET', 'POST'])
def roles_list_post(request):
    logger.info(request)
    try:
        if (request.method == 'GET'):
            from bson import json_util
            role_list = []
            data_cursor = role_collection.find()
            for data in data_cursor:
                role_list.append(json.loads(json_util.dumps(data)))
            return JsonResponse(role_list, status=200, safe=False)
        elif (request.method == 'POST'):
            existing_role = role_collection.find_one({'role_name': request.data['role_name']})
            if not existing_role:
                request.data['created_at'] = int(time.time())
                serializer = RolesSerializer(data=request.data)
                if (serializer.is_valid() == True and len(serializer.errors) == 0):
                    data = role_collection.save(request.data)
                    jsondata = {"_id": str(data)}
                    return JsonResponse(jsondata,status=201)
                else:
                    jsondata = serializer.errors
                    logger.error(jsondata)
                    return JsonResponse(jsondata, status=401)
            else:
                jsondata = {"error": "Role already exist."}
                logger.error(jsondata)
                return JsonResponse(jsondata, status=422)
    except Exception as e:
        logger.exception(e)
        jsondata = {"Error": e}
        return JsonResponse(jsondata, status=400)

@csrf_exempt
@api_view(['GET', 'PATCH', 'DELETE'])
def roles_operations(request, pk):
    logger.info(request.data)
    try:
        if (request.method == 'GET'):
            data = role_collection.find_one({'_id': ObjectId(pk)})
            if data:
                jsondata = json.loads(json_util.dumps(data))
                return JsonResponse(jsondata, status=200)
            else:
                jsondata = {"error": "Role with given ID not found."}
                logger.error(jsondata)
                return JsonResponse(jsondata, status=404)
        elif (request.method == 'PATCH'):
            serializer = RolesSerializer(data=request.data, partial=True)
            if (serializer.is_valid() == True):
                request.data['updated_at'] = int(time.time())
                update_object = role_collection.find_one_and_update({'_id': ObjectId(pk)}, {'$set': request.data})
                jsondata = json.loads(json_util.dumps(update_object))
                return JsonResponse(jsondata, status=200)
            else:
                jsondata = {"error": "Bad request body."}
                logger.error(jsondata)
                return JsonResponse(jsondata, status=400)
        elif (request.method == "DELETE"):
            delete = role_collection.delete_one({'_id': ObjectId(pk)})
            if (delete.acknowledged == True):
                jsondata = {"status": delete.acknowledged}
                return JsonResponse(jsondata, status=200)
            else:
                jsondata = {"error": "Resource does not exist."}
                logger.error(jsondata)
                return JsonResponse(jsondata, status=404)
    except Exception as e:
        jsondata = {"Exception": e}
        logger.exception(jsondata)
        return JsonResponse(jsondata, status=400)

@csrf_exempt
@api_view(['GET', 'POST'])
def users_list_post(request):
    logger.info(request)
    try:
        if (request.method == 'GET'):
            from bson import json_util
            user_list = []
            data_cursor = users_collection.find()
            for data in data_cursor:
                user_list.append(json.loads(json_util.dumps(data)))
            return JsonResponse(user_list, status=200, safe=False)
        elif (request.method == 'POST'):
            if all(key in request.data for key in ('username', 'role_name')):
                existing_user = users_collection.find_one({'username': request.data['username']})
                existing_role = role_collection.find_one({'role_name': request.data['role_name']})
                if not existing_user:
                    if existing_role:
                        request.data['created_at'] = int(time.time())
                        serializer = UsersSerializer(data=request.data)
                        if (serializer.is_valid() == True and len(serializer.errors) == 0):
                            storage_client = storage.Client.from_service_account_json('/home/gslab/Downloads/devops-padmakar-53c8fd3836c1.json')
                            bucket = storage_client.get_bucket('test_789_gcp_bucket')
                            blob = bucket.blob(request.data['username']+'/')
                            blob.upload_from_string('')
                            request.data['folder_path'] = request.data['username']+'/'
                            data = users_collection.save(request.data)
                            jsondata = {"_id": str(data)}
                            return JsonResponse(jsondata,status=201)
                        else:
                            jsondata = serializer.errors
                            logger.error(jsondata)
                            return JsonResponse(jsondata, status=422)
                    else:
                        jsondata = {"error": "Role does not exist."}
                        logger.error(jsondata)
                        return JsonResponse(jsondata, status=422)

                else:
                    jsondata = {"error": "User already exist."}
                    logger.error(jsondata)
                    return JsonResponse(jsondata, status=422)
            else:
                jsondata = {"error": "Either username or role_name is missing from request."}
                logger.error(jsondata)
                return JsonResponse(jsondata, status=422)
    except Exception as e:
        logger.exception(e)
        jsondata = {"Error": e}
        return JsonResponse(jsondata, status=400)

@csrf_exempt
@api_view(['GET', 'PATCH', 'DELETE'])
def users_operations(request, pk):
    logger.info(request.data)
    try:
        if (request.method == 'GET'):
            data = users_collection.find_one({'_id': ObjectId(pk)})
            if data:
                jsondata = json.loads(json_util.dumps(data))
                return JsonResponse(jsondata, status=200)
            else:
                jsondata = {"error": "User with given ID not found."}
                logger.error(jsondata)
                return JsonResponse(jsondata, status=404)
        elif (request.method == 'PATCH'):
            serializer = UsersSerializer(data=request.data, partial=True)
            if (serializer.is_valid() == True):
                request.data['updated_at'] = int(time.time())
                update_object = users_collection.find_one_and_update({'_id': ObjectId(pk)}, {'$set': request.data})
                data = users_collection.find_one({'_id': ObjectId(pk)})
                jsondata = json.loads(json_util.dumps(data))
                return JsonResponse(jsondata, status=200)
            else:
                jsondata = {"error": "Bad request body."}
                logger.error(jsondata)
                return JsonResponse(jsondata, status=400)
        elif (request.method == "DELETE"):
            delete = users_collection.delete_one({'_id': ObjectId(pk)})
            if (delete.acknowledged == True):
                jsondata = {"status": delete.acknowledged}
                return JsonResponse(jsondata, status=200)
            else:
                jsondata = {"error": "Resource does not exist."}
                logger.error(jsondata)
                return JsonResponse(jsondata, status=404)
    except Exception as e:
        jsondata = {"Exception": e}
        logger.exception(jsondata)
        return JsonResponse(jsondata, status=400)


@csrf_exempt
@api_view(['GET'])
def networks(request):
    logger.info(request.data)
    try:
        info = Infoblox_Service()
        networks = info.get_networks(request)
        return JsonResponse(networks, status=networks['status'])
    except Exception as e:
        logger.error(e)
        jsondata = {"Error": e}
        return JsonResponse(jsondata, status=400)


@csrf_exempt
@api_view(['GET'])
def ip_status(request):
    logger.info(request.data)
    try:
        info = Infoblox_Service()
        networks = info.get_ip_statuses(request)
        return JsonResponse(networks, status=networks['status'])
    except Exception as e:
        logger.error(e)
        jsondata = {"Error": e}
        return JsonResponse(jsondata, status=400)


@csrf_exempt
@api_view(['POST'])
def reserve_ip(request):
    logger.info(request.data)
    try:
        info = Infoblox_Service()
        networks = info.reserve_ips(request)
        return JsonResponse(networks, status=networks['status'], safe=False)
    except Exception as e:
        logger.error(e)
        jsondata = {"Error": e}
        return JsonResponse(jsondata, status=400)

@csrf_exempt
@api_view(['GET'])
def reserved_ips_list(request):
    logger.info(request.data)
    try:
        info = Infoblox_Service()
        networks = info.reserved_ips_list(request)
        return JsonResponse(networks, status=networks['status'], safe=False)
    except Exception as e:
        logger.error(e)
        jsondata = {"Error": e}
        return JsonResponse(jsondata, status=400)


@csrf_exempt
@api_view(['DELETE'])
def unreserve_ip(request):
    logger.info(request.data)
    try:
        info = Infoblox_Service()
        networks = info.unreserve_ips(request)
        return JsonResponse(networks, status=networks['status'], safe=False)
    except Exception as e:
        logger.error(e)
        jsondata = {"Error": e}
        return JsonResponse(jsondata, status=400)

@csrf_exempt
@api_view(['POST'])
def fileupload(request):
    logger.info(request.data)
    try:
        serializer = FileSerializer(data=request.data)
        if (serializer.is_valid() == True and len(serializer.errors) == 0):
            if (request.FILES['file'].size<5242880):
                file_handler = file_handler_service()
                file = file_handler.upload_file(request)
                return JsonResponse(file, status=201)
            else:
                jsondata = {"message": "File size too big. Please upload file upto 5 MB through this API."}
                logger.error(jsondata)
                return JsonResponse(jsondata, status=422)
        else:
            jsondata = serializer.errors
            logger.error(jsondata)
            return JsonResponse(jsondata, status=422)
    except Exception as e:
        logger.error(e)
        jsondata = {"Error": e}
        return JsonResponse(jsondata, status=400)

@csrf_exempt
@api_view(['POST'])
def file_big_upload(request):
    logger.info(request.data)
    try:
        serializer = FileSerializer(data=request.data)
        if (serializer.is_valid() == True and len(serializer.errors) == 0):
            if (request.FILES['file'].size<1073741824):
                file_handler = file_handler_service()
                start = time.time()
                file = file_handler.upload_file(request)
                end = time.time()
                print(end-start)
                return JsonResponse(file, status=201)
            else:
                jsondata = {"message": "File size too big. Please upload file upto 1 GB through this API."}
                logger.error(jsondata)
                return JsonResponse(jsondata, status=422)
        else:
            jsondata = serializer.errors
            logger.error(jsondata)
            return JsonResponse(jsondata, status=422)
    except Exception as e:
        logger.error(e)
        jsondata = {"Error": e}
        return JsonResponse(jsondata, status=400)


@csrf_exempt
@api_view(['GET'])
def retrieve_uploaded_files(request):
    logger.info(request.data)
    try:
        file_handler = file_handler_service()
        files = file_handler.get_uploaded_files(request)
        return JsonResponse(files, status=200)
    except Exception as e:
        logger.error(e)
        jsondata = {"Error": e}
        return JsonResponse(jsondata, status=400)

@csrf_exempt
@api_view(['GET'])
def retrieve_single_file(request):
    logger.info(request.data)
    try:
        file_handler = file_handler_service()
        files = file_handler.retrieve_file(request)
        return JsonResponse(files, status=files['status'])
    except Exception as e:
        logger.error(e)
        jsondata = {"Error": e}
        return JsonResponse(jsondata, status=400)

@csrf_exempt
@api_view(['DELETE'])
def delete_uploaded_file(request):
    logger.info(request.data)
    try:
        file_handler = file_handler_service()
        files = file_handler.delete_file(request)
        return JsonResponse(files, status=files['status'])
    except Exception as e:
        logger.error(e)
        jsondata = {"Error": e}
        return JsonResponse(jsondata, status=400)


@csrf_exempt
@api_view(['GET'])
def create_bucket(request):
    logger.info(request.data)
    try:
        bucket_handler = bucket_handler_service()
        bucket = bucket_handler.create_bucket(request)
        return JsonResponse(bucket, status=bucket['status'])
    except Exception as e:
        logger.error(e)
        jsondata = {"Error": e}
        return JsonResponse(jsondata, status=400)

@csrf_exempt
@api_view(['GET'])
def retrieve_all_buckets(request):
    logger.info(request.data)
    try:
        bucket_handler = bucket_handler_service()
        bucket = bucket_handler.retrieve_buckets(request)
        return JsonResponse(bucket, status=bucket['status'])
    except Exception as e:
        logger.error(e)
        jsondata = {"Error": e}
        return JsonResponse(jsondata, status=400)

@csrf_exempt
@api_view(['DELETE'])
def delete_bucket(request):
    logger.info(request.data)
    try:
        bucket_handler = bucket_handler_service()
        bucket = bucket_handler.delete_bucket(request)
        return JsonResponse(bucket, status=bucket['status'])
    except Exception as e:
        logger.error(e)
        jsondata = {"Error": e}
        return JsonResponse(jsondata, status=400)