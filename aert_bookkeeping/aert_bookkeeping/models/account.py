# vim: set fileencoding=utf-8

from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from django.utils.encoding import smart_text
from django.utils.encoding import python_2_unicode_compatible
from ._common_ import *


class AccountManager(models.Manager):
   def add_account(account):
      pass

   def del_account(account_id):
      pass

   def get_account_list(project_id):
      pass


@python_2_unicode_compatible
class Account(models.Model):
   name = models.CharField(_('name'), max_length=100)
   description = models.TextField(_('description'), blank=True)
   is_closed = models.BooleanField(_('is closed'), default=False)
   is_deleted = models.BooleanField(_('is deleted'), default=False)

   objects = AccountManager()

   class Meta:
      app_label = APP_LABEL
      verbose_name = _('account')
      verbose_name_plural = _('accounts')
      
   def __str__(self):
      return smart_text(self.name)
