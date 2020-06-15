import time

from google.cloud import storage

import logging

from utils.mongo_utils import MongoQueryUtils
from utils.environment_configs import EnvironmentConfigs as env

logger = logging.getLogger("django")
mongo_utils = MongoQueryUtils()

file_upload_collection = mongo_utils.get_collection_handle('file_upload')
users_collection = mongo_utils.get_collection_handle('users')

class file_handler_service:
    def upload_file(self, request):
        storage_client = storage.Client.from_service_account_json(env.google_creds)
        bucket = storage_client.get_bucket(env.bucket_id)
        user = users_collection.find_one({'username': request.query_params['username']})
        filename = "%s%s" % (user['folder_path'], request.FILES['file'].name)
        blob = bucket.blob(filename)

        upload_file = blob.upload_from_file(request.FILES['file'].file)
        file_data = {}
        file_data['file_id'] = blob.id
        file_data['bucket_id'] = blob.bucket.id
        file_data['file_name'] = blob.name
        file_data['created_at'] = int(time.time())
        uploaded_file = file_upload_collection.save(file_data)
        return {'id': str(uploaded_file), 'file_id': blob.id, 'status': 'File uploaded succesfully.'}

    def get_uploaded_files(self, request):
        get_all_files = file_upload_collection.find()
        if get_all_files:
            storage_client = storage.Client.from_service_account_json(env.google_creds)
            image_data_list = []
            for file in get_all_files:
                bucket = storage_client.get_bucket(env.bucket_id)
                blob = bucket.get_blob(file['file_name'])
                if blob:
                    # download = blob.download_to_filename('/home/gslab/Documents/'+file['file_name'])
                    image_data = {}
                    image_data['bucket_id'] = file['bucket_id']
                    image_data['file_name'] = file['file_name']
                    image_data_list.append(image_data)
                else:
                    jsondata = {}
                    jsondata['bucket_id'] = file['bucket_id']
                    jsondata['file_name'] = file['file_name']
                    jsondata['message'] = 'Image not found.'
                    jsondata['status'] = 404
                    image_data_list.append(jsondata)
            return {"images_data": image_data_list}
        else:
            jsondata = {}
            jsondata['message'] = 'Images not found.'
            jsondata['status'] = 404
            return jsondata

    def list_folder_files(self, request):
        storage_client = storage.Client.from_service_account_json(env.google_creds)
        file_list = []
        for blob in  storage_client.list_blobs(env.bucket_id,prefix=request.query_params['username']+'/'):
            print(str(blob))
            file_list.append(blob.name)
        return {"file_list": file_list}


    def delete_file(self, request):
        file = file_upload_collection.find_one({'bucket_id': env.bucket_id, 'file_name': request.query_params['file_name']})
        storage_client = storage.Client.from_service_account_json(env.google_creds)
        bucket = storage_client.get_bucket(env.bucket_id)
        blob = bucket.get_blob(file['file_name'])
        if file and blob:
            jsondata = {}
            blob.delete()
            file_upload_collection.delete_one({'_id': file['_id']})
            jsondata["message"] ='Image deleted Successfully.'
            jsondata['status'] = 200
            return jsondata
        else:
            jsondata = {}
            jsondata['message'] = 'Image not found.'
            jsondata['status'] = 404
            return jsondata

    def retrieve_file(self, request):
        file = file_upload_collection.find_one(
            {'bucket_id': env.bucket_id, 'file_name': request.query_params['file_name']})
        storage_client = storage.Client.from_service_account_json(env.google_creds)
        bucket = storage_client.get_bucket(env.bucket_id)
        blob = bucket.get_blob(request.query_params['file_name'])
        if file or blob:
            jsondata = {}
            download = blob.download_to_filename('/home/gslab/Documents/'+request.query_params['file_name'])
            jsondata['bucket_id'] = file['bucket_id']
            jsondata['file_name'] = file['file_name']
            jsondata['status'] = 200
            return jsondata
        else:
            jsondata = {}
            jsondata['message'] = 'Image not found.'
            jsondata['status'] = 404
            return jsondata

class bucket_handler_service:
    def create_bucket(self, request):
        storage_client = storage.Client.from_service_account_json(env.google_creds)
        try:
            get_bucket = storage_client.get_bucket(request.query_params['bucket_id'])
            jsondata = {}
            jsondata['message'] = 'Bucket already present with this name, try another name.'
            jsondata['bucket_id'] = request.query_params['bucket_id']
            jsondata['status'] = 422
            return jsondata
        except Exception as e:
            bucket = storage_client.create_bucket(request.query_params['bucket_id'])
            jsondata = {}
            jsondata['message'] = 'Created bucket successfully.'
            jsondata['bucket_id'] = request.query_params['bucket_id']
            jsondata['status'] = 201
            return jsondata

    def delete_bucket(self, request):
        storage_client = storage.Client.from_service_account_json(env.google_creds)
        try:
            get_bucket = storage_client.get_bucket(request.query_params['bucket_id'])
            get_bucket.delete()
            jsondata = {}
            jsondata['message'] = 'Bucket deleted successfully.'
            jsondata['bucket_id'] = request.query_params['bucket_id']
            jsondata['status'] =200
            return jsondata
        except Exception as e:
            jsondata = {}
            jsondata['message'] = 'No such bucket found or either those buckets are not empty.'
            jsondata['bucket_id'] = request.query_params['bucket_id']
            jsondata['status'] = 404
            return jsondata

    def retrieve_buckets(self, request):
        storage_client = storage.Client.from_service_account_json(env.google_creds)
        bucket_list = []
        try:
            buckets = storage_client.list_buckets()
            for bucket in buckets:
                jsondata = {}
                jsondata['bucket_id'] = bucket.id
                bucket_list.append(jsondata)
            return {'bucket_list': bucket_list, 'status': 200}
        except Exception as e:
            jsondata = {}
            jsondata['message'] = 'No such bucket found.'
            jsondata['bucket_id'] = request.query_params['bucket_id']
            jsondata['status'] = 404
            return jsondata
