# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Dictionary(models.Model):
    key = models.CharField(db_column='Key', primary_key=True, max_length=100)  # Field name made lowercase.
    shorttitle = models.CharField(db_column='shortTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    longtitle = models.CharField(db_column='LongTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contexthelp = models.CharField(db_column='ContextHelp', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dictionary'


class Portfolilables(models.Model):
    portfolilablesid = models.AutoField(db_column='portFoliLablesid', primary_key=True)  # Field name made lowercase.
    label = models.CharField(max_length=100, blank=True, null=True)
    portfolioid = models.ForeignKey('Portfolio', models.DO_NOTHING, db_column='portfolioid')

    class Meta:
        managed = False
        db_table = 'PortFoliLables'


class Portfolilinks(models.Model):
    portfolilinksid = models.AutoField(db_column='portFoliLinksid', primary_key=True)  # Field name made lowercase.
    portfolilinkslabelid = models.ForeignKey('Portfolilinkslabel', models.DO_NOTHING, db_column='portFoliLinksLabelid')  # Field name made lowercase.
    portfolioid = models.ForeignKey('Portfolio', models.DO_NOTHING, db_column='portfolioid')

    class Meta:
        managed = False
        db_table = 'PortFoliLinks'


class Portfolilinkslabel(models.Model):
    portfolilinkslabelid = models.AutoField(db_column='portFoliLinksLabelid', primary_key=True)  # Field name made lowercase.
    label = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(db_column='Url', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PortFoliLinksLabel'


class Portfolio(models.Model):
    portfolioid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    portfoliotypeid = models.ForeignKey('Portfoliotype', models.DO_NOTHING, db_column='portfolioTypeid')  # Field name made lowercase.
    owner = models.ForeignKey('Resource', models.DO_NOTHING, db_column='owner')
    teamid = models.ForeignKey('Team', models.DO_NOTHING, db_column='teamid')
    details = models.TextField(blank=True, null=True)
    rank    = models.IntegerField(db_column='rank', default=1, null=False)
    portfoliostatusid = models.ForeignKey('Portfoliostatus', models.DO_NOTHING, db_column='PortfolioStatusid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Portfolio'

class Portfoliostatus(models.Model):
    portfoliostatusid = models.AutoField(db_column='PortfolioStatusid', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return  str(self.portfoliostatusid) + ' '+ self.title  
    class Meta:
        managed = False
        db_table = 'PortfolioStatus'


class Portfoliotype(models.Model):
    portfoliotypeid = models.AutoField(db_column='portfolioTypeid', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'PortfolioType'


class Progressratio(models.Model):
    progressratioid = models.AutoField(db_column='progressRatioid', primary_key=True)  # Field name made lowercase.
    descriptions = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ProgressRatio'


class Resource(models.Model):
    resourceid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    resourcetypeid = models.ForeignKey('Resourcetype', models.DO_NOTHING, db_column='ResourceTypeid')  # Field name made lowercase.
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Resource'


class Resourcetype(models.Model):
    resourcetypeid = models.AutoField(db_column='resourceTypeid', primary_key=True)  # Field name made lowercase.
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ResourceType'


class Task(models.Model):
    taskid = models.BigAutoField(primary_key=True)
    userstoryid = models.ForeignKey('Userstory', models.DO_NOTHING, db_column='userStoryid', blank=True, null=True)  # Field name made lowercase.
    resourceid = models.ForeignKey('Teamresource', models.DO_NOTHING, db_column='Resourceid', blank=True, null=True)  # Field name made lowercase.
    estmatedstart = models.DateField(db_column='estmatedStart', blank=True, null=True)  # Field name made lowercase.
    estimatedduration = models.IntegerField(db_column='estimatedDuration', blank=True, null=True)  # Field name made lowercase.
    actualstart = models.DateField(db_column='actualStart', blank=True, null=True)  # Field name made lowercase.
    actualduration = models.IntegerField(db_column='actualDuration', blank=True, null=True)  # Field name made lowercase.
    taskstatusid = models.ForeignKey('Taskstatus', models.DO_NOTHING, db_column='taskStatusid', blank=True, null=True)  # Field name made lowercase.
    progressratioid = models.ForeignKey(Progressratio, models.DO_NOTHING, db_column='progressRatioid')  # Field name made lowercase.
    nexttaskid = models.BigIntegerField(db_column='nextTaskId', blank=True, null=True)  # Field name made lowercase.
    previoustaskid = models.BigIntegerField(db_column='previousTaskId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Task'


class Tasklinkslabel(models.Model):
    tasklinkslabelid = models.AutoField(db_column='taskLinksLabelid', primary_key=True)  # Field name made lowercase.
    label = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskLinksLabel'


class Taskstatus(models.Model):
    taskstatusid = models.AutoField(db_column='taskStatusid', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskStatus'


class Team(models.Model):
    teamid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Team'


class Teamresource(models.Model):
    resourceid = models.ForeignKey(Resource, models.DO_NOTHING, db_column='resourceid', primary_key=True)
    teamid = models.ForeignKey(Team, models.DO_NOTHING, db_column='teamid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'TeamResource'
        unique_together = (('resourceid', 'teamid'),)


class Userstory(models.Model):
    userstoryid = models.AutoField(db_column='userStoryid', primary_key=True)  # Field name made lowercase.
    details = models.CharField(max_length=100, blank=True, null=True)
    userresourceid = models.ForeignKey(Resource, models.DO_NOTHING, db_column='userResourceid')  # Field name made lowercase.
    portfolioid = models.ForeignKey('Portfolio', models.DO_NOTHING, db_column='portfolioid')
    releaseid = models.ForeignKey('Portfolireleases', models.DO_NOTHING, db_column='releaseId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserStory'


class Worklog(models.Model):
    worklogid = models.AutoField(db_column='workLogid', primary_key=True)  # Field name made lowercase.
    starttime = models.CharField(db_column='startTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    endtime = models.CharField(db_column='endTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    duration = models.CharField(db_column='Duration', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taskid = models.ForeignKey(Task, models.DO_NOTHING, db_column='taskid')

    class Meta:
        managed = False
        db_table = 'WorkLog'


class Externallinks(models.Model):
    externallinksid = models.AutoField(db_column='externalLInksid', primary_key=True)  # Field name made lowercase.
    url = models.CharField(max_length=100, blank=True, null=True)
    taskid = models.ForeignKey(Task, models.DO_NOTHING, db_column='taskid')
    linkslabelid = models.ForeignKey(Tasklinkslabel, models.DO_NOTHING, db_column='linksLabelid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'externalLInks'


class Portfolireleases(models.Model):
    portfolioid = models.ForeignKey(Portfolio, models.DO_NOTHING, db_column='portfolioid')
    releaseid = models.IntegerField(db_column='releaseId', primary_key=True)  # Field name made lowercase.
    plandate = models.DateField(db_column='planDate', blank=True, null=True)  # Field name made lowercase.
    actualdate = models.DateField(db_column='actualDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'portfoliReleases'
        unique_together = (('releaseid', 'portfolioid'),)
