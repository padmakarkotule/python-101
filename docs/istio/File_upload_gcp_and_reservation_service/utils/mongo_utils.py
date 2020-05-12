from pymongo import MongoClient
from .environment_configs import EnvironmentConfigs as EnvConfigs


class MongoQueryUtils:
    def __init__(self):
        client = MongoClient(EnvConfigs.mongo_server_ip, int(EnvConfigs.mongo_server_port))
        self.database = client[EnvConfigs.mongo_database]

    def get_collection_handle(self, colletion_name):
        collection = self.database[colletion_name]
        return collection

