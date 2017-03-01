from __future__ import unicode_literals

from django.conf import settings
from django.db import models

from common.common.models import AuditTrailCreatedUpdatedMixin, BaseDocumentMixin, ActiveMixin, QRCodeMixin


class Employee(settings.AUTH_USER_MODEL, AuditTrailCreatedUpdatedMixin, ActiveMixin, QRCodeMixin):
    """

    """
    employee_type = models.CharField(max_length=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)


class EmployeeSubjects(AuditTrailCreatedUpdatedMixin, ActiveMixin):
    """

    """
    employee = models.ForeignKey(Employee)


class EmployeeClass(AuditTrailCreatedUpdatedMixin, ActiveMixin):
    """
    """
    employee = models.ForeignKey(Employee)


class EmployeeDocument(BaseDocumentMixin):
    employee = models.ForeignKey(Employee)
