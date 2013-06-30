from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Apps
                       url(r'^', include('aert_bookkeeping.urls')),
                       # url(r'^admin/doc/',
                       #     include('django.contrib.admindocs.urls')),
                       # Admin
                       url(r'^grappelli/', include('grappelli.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )
