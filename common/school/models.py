from __future__ import unicode_literals

from django.db import models

# Create your models here.
from common.common.models import NameMixin, AuditTrailCreatedUpdatedMixin, QRCodeMixin, BaseDocumentMixin, ActiveMixin


class School(NameMixin, AuditTrailCreatedUpdatedMixin, QRCodeMixin):
    """

    """
    established_year = models.IntegerField()
    logo = models.ImageField()


class SchoolAdministration(NameMixin, AuditTrailCreatedUpdatedMixin, QRCodeMixin):
    """

    """


class SchoolDocument(BaseDocumentMixin):
    school = models.ForeignKey(School)


class AcademicYear(AuditTrailCreatedUpdatedMixin, ActiveMixin, QRCodeMixin):
    """

    """
    start_year = models.IntegerField(max_length=4)
    end_year = models.IntegerField(max_length=4)
    start_month = models.CharField(max_length=3)
    end_month = models.CharField(max_length=3)


class AcademicClass(NameMixin, AuditTrailCreatedUpdatedMixin, ActiveMixin, QRCodeMixin):
    academic_year = models.ForeignKey(AcademicYear)
    standard = models.CharField(max_length=10)
    section = models.CharField(max_length=10)
