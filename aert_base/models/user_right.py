# vim: set fileencoding=utf-8

from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from django.utils.encoding import smart_text
from django.utils.encoding import python_2_unicode_compatible
from ._common_ import *


class UserRightManager(models.Manager):
   def add_right(right):
      pass

   def del_right(right_id):
      pass


@python_2_unicode_compatible
class UserRight(models.Model):
   code = models.CharField(_('code'), max_length=100)
   name = models.CharField(_('name'), max_length=100)
   description = models.TextField(_('description'), blank=True)
   is_builtin = models.BooleanField(_('is builtin'), default=False)
   is_admin = models.BooleanField(_('is admin'), default=False)

   objects = UserRightManager()

   class Meta:
      app_label = APP_LABEL
      verbose_name = _('user right')
      verbose_name_plural = _('user rights')
      
   def __str__(self):
      return smart_text(self.name)
