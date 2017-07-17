# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Dictionary(models.Model):
    key = models.CharField(db_column='Key', primary_key=True, max_length=100)  # Field name made lowercase.
    shorttitle = models.CharField(db_column='shortTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    longtitle = models.CharField(db_column='LongTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contexthelp = models.CharField(db_column='ContextHelp', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dictionary'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Externallinks(models.Model):
    externallinksid = models.AutoField(db_column='externalLInksid', primary_key=True)  # Field name made lowercase.
    url = models.CharField(max_length=100, blank=True, null=True)
    taskid = models.ForeignKey('Task', models.DO_NOTHING, db_column='taskid')
    linkslabelid = models.ForeignKey('Tasklinkslabel', models.DO_NOTHING, db_column='linksLabelid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'externallinks'


class Portfolilables(models.Model):
    portfolilablesid = models.AutoField(db_column='portFoliLablesid', primary_key=True)  # Field name made lowercase.
    label = models.CharField(max_length=100, blank=True, null=True)
    portfolioid = models.ForeignKey('Portfolio', models.DO_NOTHING, db_column='portfolioid')

    class Meta:
        managed = False
        db_table = 'portfolilables'


class Portfolilinkslabel(models.Model):
    portfolilinkslabelid = models.AutoField(db_column='portFoliLinksLabelid', primary_key=True)  # Field name made lowercase.
    label = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(db_column='Url', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'portfolilinkslabel'


class Portfolio(models.Model):
    portfolioid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    portfoliotypeid = models.ForeignKey('Portfoliotype', models.DO_NOTHING, db_column='portfolioTypeid')  # Field name made lowercase.
    details = models.TextField(blank=True, null=True)
    rank = models.BigIntegerField()
    portfoliostatusid = models.ForeignKey('Portfoliostatus', models.DO_NOTHING, db_column='portfoliostatusid')
    owner = models.ForeignKey('Resource', models.DO_NOTHING, db_column='owner')

    class Meta:
        managed = False
        db_table = 'portfolio'
        unique_together = (('portfolioid', 'owner'),)


class Portfoliolinks(models.Model):
    portfolilinksid = models.AutoField(db_column='portFoliLinksid', primary_key=True)  # Field name made lowercase.
    portfolioid = models.ForeignKey(Portfolio, models.DO_NOTHING, db_column='portfolioid')
    portfolilinkslabelid = models.ForeignKey(Portfolilinkslabel, models.DO_NOTHING, db_column='portFoliLinksLabelid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'portfoliolinks'


class Portfolioreleases(models.Model):
    portfolioid = models.IntegerField()
    releaseid = models.AutoField(db_column='releaseid', primary_key=True)  # Field name made lowercase.
    planstartdate = models.DateField(db_column='planStartDate', blank=True, null=True)  # Field name made lowercase.
    actualstartdate = models.DateField(db_column='actualStartDate', blank=True, null=True)  # Field name made lowercase.
    teamid = models.ForeignKey('Team', models.DO_NOTHING, db_column='teamid')
    planenddate = models.DateField(db_column='planEndDate', blank=True, null=True)  # Field name made lowercase.
    actualenddate = models.DateField(db_column='actualEndDate', blank=True, null=True)  # Field name made lowercase.
    details = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portfolioreleases'


class Portfoliostatus(models.Model):
    portfoliostatusid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portfoliostatus'


class Portfoliotype(models.Model):
    portfoliotypeid = models.AutoField(db_column='portfolioTypeid', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'portfoliotype'


class Progressratio(models.Model):
    progressratioid = models.AutoField(db_column='progressRatioid', primary_key=True)  # Field name made lowercase.
    descriptions = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'progressratio'


class Resource(models.Model):
    resourceid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    active = models.IntegerField()
    teamid = models.ForeignKey('Team', models.DO_NOTHING, db_column='teamid')
    resourcetypeid = models.ForeignKey('Resourcetype', models.DO_NOTHING, db_column='resourceTypeid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resource'


class Resourcetype(models.Model):
    resourcetypeid = models.AutoField(db_column='resourceTypeid', primary_key=True)  # Field name made lowercase.
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resourcetype'


class Sprint(models.Model):
    sprintid = models.AutoField(primary_key=True)
    details = models.CharField(max_length=100, blank=True, null=True)
    startdate = models.DateField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    end = models.DateField(db_column='End', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sprint'


class Task(models.Model):
    taskid = models.BigAutoField(primary_key=True)
    userstoryid = models.ForeignKey('Userstory', models.DO_NOTHING, db_column='userStoryid', blank=True, null=True)  # Field name made lowercase.
    estmatedstart = models.DateField(db_column='estmatedStart', blank=True, null=True)  # Field name made lowercase.
    estimatedduration = models.IntegerField(db_column='estimatedDuration', blank=True, null=True)  # Field name made lowercase.
    actualstart = models.DateField(db_column='actualStart', blank=True, null=True)  # Field name made lowercase.
    actualduration = models.IntegerField(db_column='actualDuration', blank=True, null=True)  # Field name made lowercase.
    taskstatusid = models.ForeignKey('Taskstatus', models.DO_NOTHING, db_column='taskStatusid', blank=True, null=True)  # Field name made lowercase.
    progressratioid = models.ForeignKey(Progressratio, models.DO_NOTHING, db_column='progressRatioid')  # Field name made lowercase.
    nexttaskid = models.BigIntegerField(db_column='nextTaskId', blank=True, null=True)  # Field name made lowercase.
    previoustaskid = models.BigIntegerField(db_column='previousTaskId', blank=True, null=True)  # Field name made lowercase.
    resourceid = models.ForeignKey(Resource, models.DO_NOTHING, db_column='resourceid')

    class Meta:
        managed = False
        db_table = 'task'


class Tasklinkslabel(models.Model):
    tasklinkslabelid = models.AutoField(db_column='taskLinksLabelid', primary_key=True)  # Field name made lowercase.
    label = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tasklinkslabel'


class Taskstatus(models.Model):
    taskstatusid = models.AutoField(db_column='taskStatusid', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taskstatus'


class Team(models.Model):
    teamid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'team'


class Teamresource(models.Model):
    resourceid = models.ForeignKey(Resource, models.DO_NOTHING, db_column='resourceid', primary_key=True)
    teamid = models.ForeignKey(Team, models.DO_NOTHING, db_column='teamid')

    class Meta:
        managed = False
        db_table = 'teamresource'


class Userstory(models.Model):
    userstoryid = models.AutoField(db_column='userStoryid', primary_key=True)  # Field name made lowercase.
    details = models.CharField(max_length=100, blank=True, null=True)
    resourceid = models.IntegerField()
    resourceid1 = models.ForeignKey(Resource, models.DO_NOTHING, db_column='resourceid1')
    sprintid = models.ForeignKey(Sprint, models.DO_NOTHING, db_column='sprintid')
    releaseid = models.ForeignKey(Portfolioreleases, models.DO_NOTHING, db_column='releaseid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userstory'


class Worklog(models.Model):
    worklogid = models.AutoField(db_column='workLogid', primary_key=True)  # Field name made lowercase.
    starttime = models.CharField(db_column='startTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    endtime = models.CharField(db_column='endTime', max_length=100, blank=True, null=True)  # Field name made lowercase.
    duration = models.CharField(db_column='Duration', max_length=100, blank=True, null=True)  # Field name made lowercase.
    taskid = models.ForeignKey(Task, models.DO_NOTHING, db_column='taskid')

    class Meta:
        managed = False
        db_table = 'worklog'
