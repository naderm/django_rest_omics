
from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers

router = routers.DefaultRouter()

import methods.routers
import proteomics.routers
import phosphoproteomics.routers

urlpatterns = [
    url(r"^", include(router.urls)),
    url(r"^v1/", include(router.urls, namespace="api_v1")),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
