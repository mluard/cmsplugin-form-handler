# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.urls import path

from .views import ProcessFormView

app_name = 'cmsplugin_form_handler'

urlpatterns = [
    path(
        '<int:plugin_id>/',
        ProcessFormView.as_view(),
        name='process_form'
    ),
]
