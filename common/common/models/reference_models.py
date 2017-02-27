from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models

from common.common.models import AuditTrailCreatedUpdatedMixin, NameMixin


class ReferenceChoices(AuditTrailCreatedUpdatedMixin, NameMixin):
    """

    """
    choices = JSONField()


class ReferenceFacilities(AuditTrailCreatedUpdatedMixin, NameMixin):
    """

    """
    data = JSONField()


class ReferenceItems(AuditTrailCreatedUpdatedMixin, NameMixin):
    """

    """
    data = ArrayField(models.CharField(max_length=30))
