from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from myapp import views

urlpatterns = [
   path('files/upload', views.fileupload),
   path('files/retrieve_all', views.retrieve_uploaded_files),
   path('files/delete', views.delete_uploaded_file),
   path('files/retrieve_one', views.retrieve_single_file),
   path('files/list', views.list_folder_files),
   path('files/upload/big', views.file_big_upload),
   path('buckets/new', views.create_bucket),
   path('buckets/retrieve_all', views.retrieve_all_buckets),
   path('buckets/delete', views.delete_bucket),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
