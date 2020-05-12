from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from myapp import views

urlpatterns = [
   path('roles', views.roles_list_post),
   path('roles/<pk>', views.roles_operations),
   path('network', views.networks),
   path('ip_status', views.ip_status),
   path('reserve/new', views.reserve_ip),
   path('reserve/list', views.reserved_ips_list),
   path('release', views.unreserve_ip),
   path('users', views.users_list_post),
   path('users/<pk>', views.users_operations),
   path('files/upload', views.fileupload),
   path('files/retrieve_all', views.retrieve_uploaded_files),
   path('files/delete', views.delete_uploaded_file),
   path('files/retrieve_one', views.retrieve_single_file),
   path('files/upload/big', views.file_big_upload),
   path('buckets/new', views.create_bucket),
   path('buckets/retrieve_all', views.retrieve_all_buckets),
   path('buckets/delete', views.delete_bucket)
]

# urlpatterns = format_suffix_patterns(urlpatterns)
