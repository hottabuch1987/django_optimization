from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from clients.views import ClientView
from services.views import SubscriptionView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/service-auth/', include('rest_framework.urls')),   #сессии

    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

]

router = routers.DefaultRouter()
router.register(r'api/subscriptions', SubscriptionView)
router.register(r'api/client', ClientView)
urlpatterns += router.urls