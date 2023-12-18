# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.urls import include, path, re_path
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

admin.autodiscover()

urlpatterns = [
    re_path(
        r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'cmspages': CMSSitemap}}
    ),
]

urlpatterns += i18n_patterns(
    re_path(r'^admin/', admin.site.urls),
    path(
        'plugin_forms/',
        include(
            'cmsplugin_form_handler.urls',
            namespace='cmsplugin_form_handler',
        )
    ),
    path('', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
        re_path(
            r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}
        ),
    ] + staticfiles_urlpatterns() + urlpatterns
