from django.db import models

from common.common.models import NameMixin, AuditTrailCreatedUpdatedMixin, BaseDocumentMixin, QRCodeMixin


class School(NameMixin, AuditTrailCreatedUpdatedMixin, QRCodeMixin):
    """

    """
    established_year = models.IntegerField()


class SchoolDocument(BaseDocumentMixin):
    school = models.ForeignKey(School)
