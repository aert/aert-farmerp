# vim: set fileencoding=utf-8

from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from django.utils.encoding import smart_text
from django.utils.encoding import python_2_unicode_compatible
from ._common_ import *


class ExpenditureTypeManager(models.Manager):
    def add_expenditure_type(expenditure_type):
        pass

    def del_expenditure_type(expenditure_type_id):
        pass

    def get_expenditure_type_list(id):
        pass


@python_2_unicode_compatible
class ExpenditureType(models.Model):
    label_short = models.CharField(_('short label'), max_length=10)
    label_long = models.TextField(_('long label'), blank=True)
    is_builtin = models.BooleanField(_('is builtin'))

    objects = ExpenditureTypeManager()

    class Meta:
        app_label = APP_LABEL
        verbose_name = _('expenditure type')
        verbose_name_plural = _('expenditure types')

    def __str__(self):
        return smart_text(self.label_short)

