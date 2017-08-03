#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^archive/$', views.archive, name='archive'),
]
