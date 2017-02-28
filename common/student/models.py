from __future__ import unicode_literals

from django.conf import settings
from django.db import models

from common.common.models import AuditTrailCreatedUpdatedMixin, ActiveMixin
from common.course.models import AcademicYear, Term, Subject


class Student(settings.AUTH_USER_MODEL, AuditTrailCreatedUpdatedMixin, ActiveMixin):
    """

    """
    class Meta:
        proxy = True


class StudentSubscriptions(AuditTrailCreatedUpdatedMixin, ActiveMixin):
    student = models.ForeignKey(Student)


class StudentTermPerformance(models.Model, AuditTrailCreatedUpdatedMixin, ActiveMixin):
    term = models.ForeignKey(Term)


class StudentTermSubjectPerformance(models.Model):
    subject = models.ForeignKey(Subject)
    marks = models.DecimalField(decimal_places=3, max_digits=2)
    student_term = models.ForeignKey(StudentTermPerformance)
