from django.urls import path
from . import views
from django.views.i18n import JavaScriptCatalog

#urlpatterns = [
#
#]
# Create urls here

urlpatterns = [
    path('', views.homepage, name='home'),  # map home view
    # using form
    path('fbapi_uf/new/', views.fbapi_uf_new, name='fbapi_uf_new'),
    path('fbapi_uf/list/', views.fbapi_uf_list, name='fbapi_uf_list'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]