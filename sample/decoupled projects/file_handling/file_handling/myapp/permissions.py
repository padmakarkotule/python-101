import logging

logger = logging.getLogger("django")

from utils.environment_configs import EnvironmentConfigs as env

from utils.mongo_utils import MongoQueryUtils

mongo_utils = MongoQueryUtils()
network_collection = mongo_utils.get_collection_handle('networks')
reserved_ip_collection = mongo_utils.get_collection_handle(env.mongo_reserved_ips_collection)
users_collection = mongo_utils.get_collection_handle(env.mongo_users_collection)
audit_logs_collection = mongo_utils.get_collection_handle(env.mongo_audit_logs_collection)

""" Services_and_Permission:
  - Servicename: Infoblox
    Rules:
      resources:
        - path: /infoblox/ip/reserve/
          actions: GET
          role: User
	- path: /infoblox/ip/reserve
          actions: GET,POST,UPDATE,PATCH
          role: Infoblox Admin
        - path: /infoblox/ip/release 
          actions: DELETE
  - Servicename: vCenter
    Rules:
      resources:
        - path: /vCenter/dc/cluster/metrix/
	  description: 
          actions: GET
          role: vCenter.serviceAccountUser
"""

class Permission:
    @staticmethod
    def grant_user_permission(role):
        if role in env.user_roles:
            return True
        else:
            return False

    @staticmethod
    def grant_admin_permission(role):
        if role in env.admin_roles:
            return True
        else:
            return False



class vCenter:
    pass


