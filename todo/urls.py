#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^form$', views.form_test),
]
