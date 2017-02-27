from __future__ import unicode_literals

from django.db import models

from common.common.models import AuditTrailCreatedUpdatedMixin, ActiveMixin, CommonAbstractUser
from common.course.models import AcademicYear, Term, Subject

# Create your models here.


class Student(CommonAbstractUser, AuditTrailCreatedUpdatedMixin, ActiveMixin):
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
