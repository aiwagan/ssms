from __future__ import unicode_literals

from django.conf import settings
from django.db import models

from common.common.models import AuditTrailCreatedUpdatedMixin, ActiveMixin, BaseDocumentMixin, QRCodeMixin, NameMixin
from common.course.models import Term, Subject
from common.school.models import AcademicClass


class Student(settings.AUTH_USER_MODEL, AuditTrailCreatedUpdatedMixin, ActiveMixin, QRCodeMixin):
    """

    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL)


class AcademicClassStudent(AuditTrailCreatedUpdatedMixin, ActiveMixin, QRCodeMixin):
    student = models.ForeignKey(Student, unique=True)
    academic_class = models.ForeignKey(AcademicClass)


class StudentSubscription(NameMixin, AuditTrailCreatedUpdatedMixin, ActiveMixin):
    academic_class_student = models.ForeignKey(AcademicClassStudent)
    start_date = models.DateField()
    end_date = models.DateField()


class StudentTermPerformance(AuditTrailCreatedUpdatedMixin, ActiveMixin, QRCodeMixin):
    term = models.ForeignKey(Term)
    academic_class_student = models.ForeignKey(AcademicClassStudent)


class StudentTermSubjectPerformance(AuditTrailCreatedUpdatedMixin, ActiveMixin, QRCodeMixin):
    subject = models.ForeignKey(Subject)
    marks = models.DecimalField(decimal_places=3, max_digits=2)
    student_term = models.ForeignKey(StudentTermPerformance)


class StudentDocument(BaseDocumentMixin):
    """

    """
    academic_class_student = models.ForeignKey(AcademicClassStudent)
