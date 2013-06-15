from django.conf.urls import patterns, include, url
#from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('aert_bookkeeping_core.views',
                       url(r'^$', 'home', name='home'),
                       # Examples:
                       # url(r'^aert_bookkeeping_site/', include('aert_bookkeeping_site.foo.urls')),

                       )
