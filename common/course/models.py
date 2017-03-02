from __future__ import unicode_literals

from django.db import models

from common.common.models import (AuditTrailCreatedUpdatedMixin, ActiveMixin,
                                  NameMixin, QRCodeMixin, )
from common.school.models import AcademicYear


class Course(NameMixin, AuditTrailCreatedUpdatedMixin, ActiveMixin, QRCodeMixin):
    academic_year = models.ForeignKey(AcademicYear)


class Subject(NameMixin, AuditTrailCreatedUpdatedMixin, ActiveMixin, QRCodeMixin):
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course)


class Lesson(NameMixin, AuditTrailCreatedUpdatedMixin, ActiveMixin):
    name = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject)


class Term(NameMixin, AuditTrailCreatedUpdatedMixin, ActiveMixin):
    academic_year = models.ForeignKey(AcademicYear)
