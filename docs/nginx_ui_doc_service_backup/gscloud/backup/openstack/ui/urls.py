from django.urls import path
from . import views
from django.views.i18n import JavaScriptCatalog
from django.conf.urls.static import static
from django.conf import settings
#urlpatterns = [
#
#]
# Create urls here

urlpatterns = [
    path('', views.homepage, name='home'),  # map home view
    path('homepagetest/', views.homepagetest, name='hometest'),  # map home view
    path('docs/', views.docs, name='documentation'),  # map documentation view
    # path('static/', views.static, name='static'),  # map documentation view
    path('servicedesk/', views.servicedesk, name='servicedesk'),  # map documentation view
    # using form
    path('fbapi_uf/new/', views.fbapi_uf_new, name='fbapi_uf_new'),
    path('fbapi_uf/list/', views.fbapi_uf_list, name='fbapi_uf_list'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)