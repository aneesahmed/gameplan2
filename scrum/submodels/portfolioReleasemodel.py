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
from scrum.submodels.portfoliomodel import Portfolio
from scrum.submodels.teammodel import Resource,Team,TeamResource
from  datetime import  date
from django.contrib.auth.models import User
#--------- ends of import
# need a user story list with status filter (active, unassigned, )
# filter by projects
#filter by users (assign to me, current user)


class ReleaseStatus(models.Model):
    releasestatusid = models.AutoField(db_column='releasestatusid', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='title', max_length=100, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return   self.title
    class Meta:
        managed = False
        db_table = 'ReleaseStatus'

class PortfolioReleases(models.Model):
    portfolioid = models.ForeignKey(Portfolio, models.DO_NOTHING, db_column='portfolioid')
    releaseid = models.AutoField(db_column='releaseid', primary_key=True)  # Field name made lowercase.
    planstartdate = models.DateField(db_column='planStartDate', blank=True, null=True)  # Field name made lowercase.
    actualstartdate = models.DateField(db_column='actualStartDate', blank=True, null=True)  # Field name made lowercase.
    teamid = models.ForeignKey(Team, models.DO_NOTHING, db_column='teamid')
    planenddate = models.DateField(db_column='planEndDate', blank=True, null=True)  # Field name made lowercase.
    actualenddate = models.DateField(db_column='actualEndDate', blank=True, null=True)  # Field name made lowercase.
    details = models.CharField(max_length=100, blank=True, null=True)
    releasestatusid = models.ForeignKey('ReleaseStatus', models.DO_NOTHING, db_column='releasestatusid')  # Field name made lowercase.
    createby = models.CharField(max_length=100)
    createdate = models.DateField(db_column='createDate', blank=True, null=True, default=date.today)  # Field name made lowercase.
    updateby = models.CharField(max_length=100)
    updatedate = models.DateField(db_column='updatedate', blank=True, null=True, default=date.today)  # Field name made lowercase.

    def get_absolute_url(self):
        return reverse('scrum:portfolio-detail', args=[self.portfolioid_id])


        #return reverse('releaseList')
    def __str__(self):
        return str(self.portfolioid ) + ':' +     str(self.releaseid)

    class Meta:
        managed = False
        db_table = 'portfolioReleases'

class Sprint(models.Model):
    sprintid = models.AutoField(primary_key=True)
    details = models.CharField(max_length=100, blank=True, null=True)
    startdate = models.DateField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='End', blank=True, null=True)  # Field name made lowercase.
    releaseid = models.ForeignKey(PortfolioReleases, models.DO_NOTHING, db_column='releaseid', default=1)
    createby = models.CharField(max_length=100, blank=True, null=True)
    createdate = models.DateField(db_column='createDate', blank=True, null=True, default=date.today)  # Field name made lowercase.
    updateby = models.CharField(max_length=100, blank=True, null=True)
    updatedate = models.DateField(db_column='updatedate', blank=True, null=True, default=date.today)  # Field name made lowercase.

    def get_absolute_url(self):
        return reverse('scrum:release-detail', args=[self.releaseid_id])

    def __str__(self):
        return str(self.releaseid) + ':' + str(self.sprintid) + ':' + self.details

    class Meta:
        managed = False
        db_table = 'sprint'

class Userstory(models.Model):
    userstoryid = models.AutoField(db_column='userstoryid', primary_key=True)  # Field name made lowercase.
    details = models.CharField(max_length=100, blank=True, null=True)
    sprintid = models.ForeignKey(Sprint, models.DO_NOTHING, db_column='sprintid',blank=True, null=True)
    releaseid = models.ForeignKey(PortfolioReleases, models.DO_NOTHING, db_column='releaseid', default=1)
    createby = models.CharField(max_length=100, blank=True, null=True)
    createdate = models.DateField(db_column='createDate', blank=True, null=True, default=date.today)  # Field name made lowercase.
    updateby = models.CharField(max_length=100, blank=True, null=True)
    updatedate = models.DateField(db_column='updatedate', blank=True, null=True, default=date.today)  # Field name made lowercase.

    def get_absolute_url(self):
        return reverse('scrum:release-detail', args=[self.releaseid_id])

    class Meta:
        managed = False
        db_table = 'userstory'
        ordering = ["-userstoryid"]

    def __str__(self):  # __unicode__ on Python 2
        return self.details


class TaskStatus(models.Model):
    taskstatusid = models.AutoField(db_column='taskStatusid', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.title
    class Meta:
        managed = False
        db_table = 'TaskStatus'

class Task(models.Model):
    taskid = models.BigAutoField(primary_key=True)
    details =models.CharField(max_length=100, blank=True, null=True)
    userstoryid = models.ForeignKey('Userstory', models.DO_NOTHING, db_column='userStoryid', blank=True, null=True)  # Field name made lowercase.
    resourceid =  models.CharField(max_length=100, blank=True, null=True)  # Field name made lowercase.
    estmatedstart = models.DateField(db_column='estmatedstart', blank=True, null=True, default=date.today)  # Field name made lowercase.
    estimatedduration = models.IntegerField(db_column='estimatedDuration', blank=True, null=True)  # Field name made lowercase.
    actualstart = models.DateField(db_column='actualstart', blank=True, null=True, default=date.today)  # Field name made lowercase.
    actualduration = models.IntegerField(db_column='actualDuration', blank=True, null=True)  # Field name made lowercase.
    taskstatusid = models.ForeignKey('Taskstatus', models.DO_NOTHING, db_column='taskStatusid', blank=True, null=True)  # Field name made lowercase.
    progressratioid = models.IntegerField(db_column='progressratioid', blank=True, null=True, default=0)    # Field name made lowercase.
    #nexttaskid = models.BigIntegerField(db_column='nextTaskId', blank=True, null=True)  # Field name made lowercase.
    #previoustaskid = models.BigIntegerField(db_column='previousTaskId', blank=True, null=True)  # Field name made lowercase.

    def get_absolute_url(self):
        return reverse('scrum:userstory-detail', args=[self.userstoryid_id])

    class Meta:
        managed = False
        db_table = 'Task'
