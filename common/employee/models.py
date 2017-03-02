from __future__ import unicode_literals

from django.conf import settings
from django.db import models

from common.common.models import AuditTrailCreatedUpdatedMixin, BaseDocumentMixin, ActiveMixin, QRCodeMixin
from common.school.models import AcademicYear, AcademicClass


class Employee(settings.AUTH_USER_MODEL, AuditTrailCreatedUpdatedMixin, ActiveMixin, QRCodeMixin):
    """

    """
    employee_type = models.CharField(max_length=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)


class AcademicEmployee(AuditTrailCreatedUpdatedMixin, ActiveMixin, QRCodeMixin):
    employee = models.ForeignKey(Employee)
    academic_year = models.ForeignKey(AcademicYear)


class AcademicClassEmployee(AuditTrailCreatedUpdatedMixin, ActiveMixin, QRCodeMixin):
    employee = models.ForeignKey(Employee)
    academic_class = models.ForeignKey(AcademicClass)


class EmployeeSubjects(AuditTrailCreatedUpdatedMixin, ActiveMixin):
    """

    """
    academic_employee = models.ForeignKey(AcademicEmployee)


class EmployeeClass(AuditTrailCreatedUpdatedMixin, ActiveMixin):
    """
    """
    academic_class_employee = models.ForeignKey(AcademicClass)


class EmployeeDocument(BaseDocumentMixin):
    academic_employee = models.ForeignKey(AcademicEmployee)
