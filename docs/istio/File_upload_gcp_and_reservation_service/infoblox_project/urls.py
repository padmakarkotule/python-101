
from django.conf.urls import url, include

urlpatterns = [

]
urlpatterns.append(url(r'^api/', include('myapp.urls')))

