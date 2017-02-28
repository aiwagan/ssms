from __future__ import unicode_literals

from django.db import models

from common.common.models import AuditTrailCreatedUpdatedMixin, ActiveMixin, NameMixin


class AcademicYear(AuditTrailCreatedUpdatedMixin, ActiveMixin):
    """

    """
    start_year = models.IntegerField(max_length=4)
    end_year = models.IntegerField(max_length=4)
    start_month = models.CharField(max_length=3)
    end_month = models.CharField(max_length=3)


class Course(NameMixin, AuditTrailCreatedUpdatedMixin, ActiveMixin):
    academic_year = models.ForeignKey(AcademicYear)


class Subject(NameMixin, AuditTrailCreatedUpdatedMixin, ActiveMixin):
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course)


class Lesson(NameMixin, AuditTrailCreatedUpdatedMixin, ActiveMixin):
    name = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject)


class Standard(NameMixin, AuditTrailCreatedUpdatedMixin, ActiveMixin):
    pass


class Section(NameMixin, AuditTrailCreatedUpdatedMixin, ActiveMixin):
    pass


class Term(NameMixin, AuditTrailCreatedUpdatedMixin, ActiveMixin):
    academic_year = models.ForeignKey(AcademicYear)
