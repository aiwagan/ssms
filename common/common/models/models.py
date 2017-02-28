from __future__ import unicode_literals

from django.conf import settings
from django.db import models


class AuditTrailCreatedMixin(models.Model):
    """

    """
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_by')
    created_date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class AuditTrailUpdatedMixin(models.Model):
    """

    """
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='updated_by')
    updated_date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class AuditTrailCreatedUpdatedMixin(AuditTrailCreatedMixin, AuditTrailUpdatedMixin):
    """

    """
    pass


class ActiveMixin(models.Model):
    """

    """
    active = models.BooleanField(default=False)

    class Meta:
        abstract = True


class NameMixin(models.Model):
    """

    """
    name = models.CharField(max_length=50)

    class Meta:
        abstract = True
