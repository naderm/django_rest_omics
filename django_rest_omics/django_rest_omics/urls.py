
from django.conf.urls import patterns, include, url
from django.contrib import admin

import rest_framework

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include(rest_framework.urls, namespace='rest_framework')),
)
