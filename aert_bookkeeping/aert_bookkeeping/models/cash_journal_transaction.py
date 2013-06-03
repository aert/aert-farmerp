# vim: set fileencoding=utf-8

from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from django.utils.encoding import smart_text
from django.utils.encoding import python_2_unicode_compatible
from ._common_ import *


class CashJournalTransactionManager(models.Manager):
   def add_transaction(cash_journal_transaction):
      pass

   def del_transaction(cash_journal_transaction_id):
      pass

   def get_transaction_list(cash_journal_id):
      pass


@python_2_unicode_compatible
class CashJournalTransaction(models.Model):
   transaction_type = models.PositiveSmallIntegerField(_('transaction type'))
   transaction_date = models.DateTimeField(_('transaction date', auto_now=True))
   amount = models.DecimalField(_('amount'), max_digits=15, decimal_places=2, default=0)
   comment = models.TextField(_('comment'), blank=True)

   objects = CashJournalTransactionManager()

   class Meta:
      app_label = APP_LABEL
      verbose_name = _('cash journal transaction')
      verbose_name_plural = _('cash journal transactions')
      ordering = ('-transaction_date',)
      
   def __str__(self):
      if self.transaction_type == DEBIT:
         ttype = 'DEBIT'
      elif self.transaction_type == CREDIT:
         ttype = 'CREDIT'
      else:
         ttype = 'UNKNOWN'

      return ugettext('%(date) - ' + ttype) % {
            'date': smart_text(self.transaction_date),
      }

