from django.contrib.auth.decorators import login_required


@login_required
def home(req):
    pass

@login_required
def cash_journal(req):
    pass

@login_required
def credit_book(req):
    pass

@login_required
def accounts(req):
    pass
