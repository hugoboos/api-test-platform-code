from django.urls import path, include

from vng.servervalidation import api_views, apps

app_name = apps.AppConfig.__name__

urlpatterns = [
    path('', include("vng.api.v1.servervalidation.routes", namespace="provider")),
    path('provider-run-shield/<uuid:uuid>/', api_views.ResultServerViewShield.as_view(), name='api_server-run-shield'),
    path('provider-latest-badge/<uuid:uuid>/', api_views.ServerRunLatestResultView.as_view(), name='latest-badge'),
    path('provider-run/<uuid:uuid>/result', api_views.ResultServerView.as_view(), name='provider_result'),
]
