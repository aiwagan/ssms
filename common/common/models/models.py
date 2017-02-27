from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from django.db import models

import common.common.constants


# Create your models here.


class AuditTrailCreatedMixin(models.Model):
    """

    """
    created_by = models.ForeignKey(User, related_name='created_by')
    created_date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class AuditTrailUpdatedMixin(models.Model):
    """

    """
    updated_by = models.ForeignKey(User, related_name='updated_by')
    updated_date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class AuditTrailCreatedUpdatedMixin(AuditTrailCreatedMixin, AuditTrailUpdatedMixin):
    """

    """
    pass


class ActiveMixin(models.Model):
    """

    """
    active = models.BooleanField(default=False)

    class Meta:
        abstract = True


class NameMixin(models.Model):
    """

    """
    name = models.CharField(max_length=50)

    class Meta:
        abstract = True


class Address(models.Model):
    line_1 = models.CharField(max_length=100)
    line_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    zip_code = models.IntegerField(max_length=6)
    address_type = models.CharField(max_length=1, choices=common.common.constants.ADDRESS_TYPE_CHOICES)
    fixed_line_number = models.CharField(max_length=10)
    fixed_line_area_code = models.IntegerField(max_length=5)


class CommonAbstractUser(AbstractUser, AuditTrailCreatedUpdatedMixin):
    """

    """
    mobile_number = models.IntegerField(max_length=10)
    country_code = models.IntegerField(default=91)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=common.common.constants.GENDER_CHOICES)
    photo = models.FileField(upload_to=settings.UPLOAD_AVATARS_TO)
    blood_group = models.CharField(max_length=10, choices=common.common.constants.BLOOD_GROUP_CHOICES)
    user_type = models.CharField(max_length=1, choices=common.common.constants.USER_TYPE_CHOICES)


