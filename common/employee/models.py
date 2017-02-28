from __future__ import unicode_literals

from django.conf import settings
from django.db import models


class Employee(settings.AUTH_USER_MODEL):
    """

    """


class EmployeeSubjects(models.Model):
    """

    """


class EmployeeClass(models.Model):
    """
    """


class Teacher(settings.AUTH_USER_MODEL):
    """

    """
    def __init__(self, *args, **kwargs):
        super(Teacher, self).__init__(*args, **kwargs)
        self.user_type = 'T'

    class Meta:
        proxy = True
