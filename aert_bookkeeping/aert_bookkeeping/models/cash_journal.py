# vim: set fileencoding=utf-8

from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from django.utils.encoding import smart_text
from django.utils.encoding import python_2_unicode_compatible
from ._common_ import *


class CashJournalManager(models.Manager):
   def add_cash_journal(cash_journal):
      pass

   def del_cash_journal(cash_journal_id):
      pass

   def get_cash_journal_last(project_id):
      pass

   def get_cash_journal_list(project_id):
      pass


@python_2_unicode_compatible
class CashJournal(models.Model):
   start_date = models.DateField(_('start date'))
   end_date = models.DateField(_('end date'))
   balance_forward = models.DecimalField(_('balance forward'), max_digits=15, decimal_places=2, default=0)
   comment = models.TextField(_('comment'), blank=True)
   is_deleted = models.BooleanField(_('is deleted'), default=False)

   objects = CashJournalManager()

   class Meta:
      app_label = APP_LABEL
      verbose_name = _('cash journal')
      verbose_name_plural = _('cash journals')
      ordering = ('-start_date',)
      
   def __str__(self):
      return ugettext('From %(start_date) to %(end_date)') % {
            'start_date': smart_text(self.start_date),
            'end_date': smart_text(self.end_date),
      }
