# coding=utf-8
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.urls import reverse
from django.db import models
from scrum.submodels.portfoliomodel import PortfolioReleases
from scrum.submodels.sprintmodel import Sprint
from scrum.submodels.teammodel import Resource

#--------- ends of import
# need a user story list with status filter (active, unassigned, )
# filter by projects
#filter by users (assign to me, current user)

class Userstory(models.Model):
    userstoryid = models.AutoField(db_column='userstoryid', primary_key=True)  # Field name made lowercase.
    details = models.CharField(max_length=100, blank=True, null=True)
    resourceid = models.ForeignKey(Resource, models.DO_NOTHING, db_column='resourceid1')
    sprintid = models.ForeignKey(Sprint, models.DO_NOTHING, db_column='sprintid')
    releaseId = models.ForeignKey(PortfolioReleases, models.DO_NOTHING, db_column='releaseid')


    class Meta:
        managed = False
        db_table = 'userstory'
        ordering = ["-userstoryid"]

    def __str__(self):  # __unicode__ on Python 2
        return self.name