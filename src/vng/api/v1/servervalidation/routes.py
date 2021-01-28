from rest_framework import routers
from django.urls import path, include

from vng.servervalidation import api_views, apps

app_name = apps.AppConfig.__name__

router = routers.DefaultRouter(trailing_slash=False)
router.register('provider-run', api_views.ServerRunViewSet, base_name='api_server-run')
router.register('postman-test', api_views.PostmanTestViewset, base_name='api_postman-test')

urlpatterns = router.urls
