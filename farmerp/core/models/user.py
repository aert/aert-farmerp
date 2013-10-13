from django.db import models
from django.utils.html import force_text
#from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib import auth
#from django.contrib.auth.models import User


#class User(models.Model):
#
#    def reload(self):
#        self.name = None
#        self.projects_by_role = None
#        self.membership_by_project_id=None
#        builtin_role = None

class UserManager(models.Manager):

    def try_to_login(self, request, login, password, active_only=True):
        '''Returns the user that matches provided login and pwd, or None'''
        login = force_text(login)
        password = force_text(password)

        # Make sure no one can sign in with an empty login or password
        if not login or not password:
            return None

        user = auth.authenticate(login, password)
        if not user or (not user.active and active_only):
            return None
        auth.login(request, user)
        return user
