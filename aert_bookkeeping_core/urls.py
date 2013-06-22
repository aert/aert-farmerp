from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('aert_bookkeeping_core.views',
        #url(r'^$', 'home', name='home'),
        url(r'^$', TemplateView.as_view(template_name='base.html'), name='home'),
        url(r'^cash-journal', 'cash_journal', name='cash_journal'),
        url(r'^credit-book', 'credit_book', name='credit_book'),
        url(r'^accounts', 'accounts', name='accounts'),
        )
