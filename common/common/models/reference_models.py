from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models

from common.common.models import AuditTrailCreatedUpdatedMixin, NameMixin


class ReferenceChoice(AuditTrailCreatedUpdatedMixin, NameMixin):
    """

    """
    choices = JSONField()


class ReferenceFacility(AuditTrailCreatedUpdatedMixin, NameMixin):
    """

    """
    data = JSONField()


class ReferenceItem(AuditTrailCreatedUpdatedMixin, NameMixin):
    """

    """
    data = ArrayField(models.CharField(max_length=30))


class ReferenceDepartment(AuditTrailCreatedUpdatedMixin, NameMixin):
    """

    """
    pass


class ReferenceDesignation(AuditTrailCreatedUpdatedMixin, NameMixin):
    """

    """
    pass
