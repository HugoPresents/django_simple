from django.conf.urls import patterns, include, url

from django_simple.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simple.views.home', name='home'),
    # url(r'^simple/', include('simple.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^hello/$', hello),
    (r'^now/$', now),
    (r'^now/plus/(\d)/$', now_plus),
    (r'^index/$', index),
)
