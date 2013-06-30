from django.contrib import admin
from .models import *


admin.site.register(UserRight)
admin.site.register(Project)
admin.site.register(Account)
admin.site.register(CashJournal)
admin.site.register(ExpenditureType)
admin.site.register(CashJournalTransaction)
admin.site.register(CreditBookTransaction)
