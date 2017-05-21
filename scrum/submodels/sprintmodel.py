# coding=utf-8
from __future__ import unicode_literals
from django.urls import reverse
from django.db import models

class Sprint(models.Model):
    sprintid = models.AutoField(primary_key=True)
    details = models.CharField(max_length=100, blank=True, null=True)
    startdate = models.DateField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    end = models.DateField(db_column='End', blank=True, null=True)  # Field name made lowercase.
