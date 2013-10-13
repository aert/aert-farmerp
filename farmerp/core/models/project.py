# vim: set fileencoding=utf-8

from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from django.utils.encoding import smart_text
from django.utils.encoding import python_2_unicode_compatible
from ._common_ import *


class ProjectManager(models.Manager):
    def add_project(project):
        pass

    def del_project(project_id):
        pass

    def get_project_list():
        pass


@python_2_unicode_compatible
class Project(models.Model):
    code = models.CharField(_('code'), max_length=100)
    name = models.CharField(_('name'), max_length=100)
    start_date = models.DateField(_('start_date'), auto_now_add=True)
    description = models.TextField(_('description'), blank=True)
    is_archived = models.BooleanField(_('is archived'), default=False)
    is_deleted = models.BooleanField(_('is deleted'), default=False)

    objects = ProjectManager()

    class Meta:
        app_label = APP_LABEL
        verbose_name = _('project')
        verbose_name_plural = _('projects')

    def __str__(self):
        return smart_text(self.name)
