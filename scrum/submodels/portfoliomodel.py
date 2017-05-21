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
#from scrum.submodels.userstorymodel import
from scrum.submodels.teammodel import Team

class Dictionary(models.Model):
    key = models.CharField(db_column='Key', primary_key=True, max_length=100)  # Field name made lowercase.
    shorttitle = models.CharField(db_column='shortTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    longtitle = models.CharField(db_column='LongTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contexthelp = models.CharField(db_column='ContextHelp', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dictionary'

class Portfoliolables(models.Model):
    portfoliolablesid = models.AutoField(db_column='portfolioLablesid', primary_key=True)  # Field name made lowercase.
    label = models.CharField(max_length=100, blank=True, null=True)
    portfolioid = models.ForeignKey('Portfolio', models.DO_NOTHING, db_column='portfolioid')


    class Meta:
        managed = False
        db_table = 'PortfoliLables'


class PortfolioLinks(models.Model):
    portfolioLinksid = models.AutoField(db_column='portfolioLinksid', primary_key=True)  # Field name made lowercase.
    portfolioLinksLabelid = models.ForeignKey('PortfolioLinksLabel', models.DO_NOTHING, db_column='portfoliolinkslabelid')  # Field name made lowercase.
    portfolioid = models.ForeignKey('Portfolio', models.DO_NOTHING, db_column='portfolioid')

    class Meta:
        managed = False
        db_table = 'PortfolioLinks'


class PortfolioLinksLabel(models.Model):
    portfolioLinkslabelid = models.AutoField(db_column='portfoliolinkslabelid', primary_key=True)  # Field name made lowercase.
    label = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(db_column='Url', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'portfoliolinkslabelid'


class Portfolio(models.Model):
    portfolioid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    portfoliotypeid = models.ForeignKey('Portfoliotype', models.DO_NOTHING, db_column='portfolioTypeid')  # Field name made lowercase.
    owner = models.ForeignKey('Resource', models.DO_NOTHING, db_column='owner' )
    details = models.TextField(blank=True, null=True)
    rank    = models.IntegerField(db_column='rank', default=1, null=False)
    portfoliostatusid = models.ForeignKey('PortfolioStatus', models.DO_NOTHING, db_column='PortfolioStatusid')  # Field name made lowercase.

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('portfolio-detail', args=[str(self.portfolioid)])

    def __str__(self):
        return  self.title
    class Meta:
        managed = False
        db_table = 'Portfolio'


class PortfolioStatus(models.Model):
    portfoliostatusid = models.AutoField(db_column='PortfolioStatusid', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return   self.title
    class Meta:
        managed = False
        db_table = 'PortfolioStatus'


class PortfolioType(models.Model):
    portfoliotypeid = models.AutoField(db_column='portfolioTypeid', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=100)


    class Meta:
        managed = False
        db_table = 'PortfolioType'
    def __str__(self):
        return   self.title

class ProgressRatio(models.Model):
    progressratioid = models.AutoField(db_column='progressRatioid', primary_key=True)  # Field name made lowercase.
    descriptions = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ProgressRatio'



class Task(models.Model):
    taskid = models.BigAutoField(primary_key=True)
    userstoryid = models.ForeignKey('Userstory', models.DO_NOTHING, db_column='userStoryid', blank=True, null=True)  # Field name made lowercase.
    resourceid = models.ForeignKey('Teamresource', models.DO_NOTHING, db_column='Resourceid', blank=True, null=True)  # Field name made lowercase.
    estmatedstart = models.DateField(db_column='estmatedStart', blank=True, null=True)  # Field name made lowercase.
    estimatedduration = models.IntegerField(db_column='estimatedDuration', blank=True, null=True)  # Field name made lowercase.
    actualstart = models.DateField(db_column='actualStart', blank=True, null=True)  # Field name made lowercase.
    actualduration = models.IntegerField(db_column='actualDuration', blank=True, null=True)  # Field name made lowercase.
    taskstatusid = models.ForeignKey('Taskstatus', models.DO_NOTHING, db_column='taskStatusid', blank=True, null=True)  # Field name made lowercase.
    progressratioid = models.ForeignKey(ProgressRatio, models.DO_NOTHING, db_column='progressratioid')  # Field name made lowercase.
    nexttaskid = models.BigIntegerField(db_column='nextTaskId', blank=True, null=True)  # Field name made lowercase.
    previoustaskid = models.BigIntegerField(db_column='previousTaskId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Task'



class TaskStatus(models.Model):
    taskstatusid = models.AutoField(db_column='taskStatusid', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskStatus'


class PortfolioReleases(models.Model):
    portfolioid = models.ForeignKey(Portfolio, models.DO_NOTHING, db_column='portfolioid')
    releaseid = models.AutoField(db_column='releaseId', primary_key=True)  # Field name made lowercase.
    planstartdate = models.DateField(db_column='planStartDate', blank=True, null=True)  # Field name made lowercase.
    actualstartdate = models.DateField(db_column='actualStartDate', blank=True, null=True)  # Field name made lowercase.
    teamid = models.ForeignKey(Team, models.DO_NOTHING, db_column='teamid')
    planenddate = models.DateField(db_column='planEndDate', blank=True, null=True)  # Field name made lowercase.
    actualenddate = models.DateField(db_column='actualEndDate', blank=True, null=True)  # Field name made lowercase.
    details = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portfolioreleases'

    def __str__(self):
        return  self.details
    class Meta:
        managed = False
        db_table = 'portfolioReleases'



class WorkLog(models.Model):
    worklogid = models.AutoField(db_column='workLogid', primary_key=True)  # Field name made lowercase.
    starttime = models.CharField(db_column='startTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    endtime = models.CharField(db_column='endTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    duration = models.CharField(db_column='Duration', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taskid = models.ForeignKey(Task, models.DO_NOTHING, db_column='taskid')

    class Meta:
        managed = False
        db_table = 'WorkLog'


class TaskLinksLabel(models.Model):
    tasklinkslabelid = models.AutoField(db_column='tasklinkslabelid', primary_key=True)  # Field name made lowercase.
    label = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tasklinkslabel'

class ExternalLinks(models.Model):
    externallinksid = models.AutoField(db_column='externallinksid', primary_key=True)  # Field name made lowercase.
    urltext      = models.CharField(max_length=100, blank=True, null=True)
    taskid = models.ForeignKey(Task, models.DO_NOTHING, db_column='taskid')
    linkslabelid = models.ForeignKey(TaskLinksLabel, models.DO_NOTHING, db_column='tasklinkslabelid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'externalLInks'

