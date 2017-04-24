# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=30, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('key', models.CharField(primary_key=True, max_length=100, db_column='Key', serialize=False)),
                ('shorttitle', models.CharField(blank=True, db_column='shortTitle', null=True, max_length=100)),
                ('longtitle', models.CharField(blank=True, db_column='LongTitle', null=True, max_length=100)),
                ('contexthelp', models.CharField(blank=True, db_column='ContextHelp', null=True, max_length=100)),
            ],
            options={
                'db_table': 'Dictionary',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(primary_key=True, max_length=40, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Externallinks',
            fields=[
                ('externallinksid', models.AutoField(primary_key=True, db_column='externalLInksid', serialize=False)),
                ('url', models.CharField(blank=True, null=True, max_length=100)),
            ],
            options={
                'db_table': 'externalLInks',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Portfolilables',
            fields=[
                ('portfolilablesid', models.AutoField(primary_key=True, db_column='portFoliLablesid', serialize=False)),
                ('label', models.CharField(blank=True, null=True, max_length=100)),
            ],
            options={
                'db_table': 'PortFoliLables',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Portfolilinks',
            fields=[
                ('portfolilinksid', models.AutoField(primary_key=True, db_column='portFoliLinksid', serialize=False)),
            ],
            options={
                'db_table': 'PortFoliLinks',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Portfolilinkslabel',
            fields=[
                ('portfolilinkslabelid', models.AutoField(primary_key=True, db_column='portFoliLinksLabelid', serialize=False)),
                ('label', models.CharField(blank=True, null=True, max_length=100)),
                ('url', models.CharField(blank=True, db_column='Url', null=True, max_length=100)),
            ],
            options={
                'db_table': 'PortFoliLinksLabel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('portfolioid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('details', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Portfolio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Portfoliotype',
            fields=[
                ('portfoliotypeid', models.AutoField(primary_key=True, db_column='portfolioTypeid', serialize=False)),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'PortfolioType',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Progressratio',
            fields=[
                ('progressratioid', models.AutoField(primary_key=True, db_column='progressRatioid', serialize=False)),
                ('descriptions', models.CharField(blank=True, null=True, max_length=100)),
            ],
            options={
                'db_table': 'ProgressRatio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('resourceid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('active', models.IntegerField()),
            ],
            options={
                'db_table': 'Resource',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Resourcetype',
            fields=[
                ('resourcetypeid', models.AutoField(primary_key=True, db_column='resourceTypeid', serialize=False)),
                ('description', models.CharField(blank=True, null=True, max_length=100)),
            ],
            options={
                'db_table': 'ResourceType',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('taskid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('estmatedstart', models.DateField(blank=True, db_column='estmatedStart', null=True)),
                ('estimatedduration', models.IntegerField(blank=True, db_column='estimatedDuration', null=True)),
                ('actualstart', models.DateField(blank=True, db_column='actualStart', null=True)),
                ('actualduration', models.IntegerField(blank=True, db_column='actualDuration', null=True)),
                ('nexttaskid', models.BigIntegerField(blank=True, db_column='nextTaskId', null=True)),
                ('previoustaskid', models.BigIntegerField(blank=True, db_column='previousTaskId', null=True)),
            ],
            options={
                'db_table': 'Task',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tasklinkslabel',
            fields=[
                ('tasklinkslabelid', models.AutoField(primary_key=True, db_column='taskLinksLabelid', serialize=False)),
                ('label', models.CharField(blank=True, null=True, max_length=100)),
            ],
            options={
                'db_table': 'TaskLinksLabel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Taskstatus',
            fields=[
                ('taskstatusid', models.AutoField(primary_key=True, db_column='taskStatusid', serialize=False)),
                ('title', models.CharField(blank=True, null=True, max_length=100)),
            ],
            options={
                'db_table': 'TaskStatus',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('teamid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Team',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teamresource',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
            ],
            options={
                'db_table': 'TeamResource',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Userstory',
            fields=[
                ('userstoryid', models.AutoField(primary_key=True, db_column='userStoryid', serialize=False)),
                ('details', models.CharField(blank=True, null=True, max_length=100)),
            ],
            options={
                'db_table': 'UserStory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Worklog',
            fields=[
                ('worklogid', models.AutoField(primary_key=True, db_column='workLogid', serialize=False)),
                ('starttime', models.CharField(blank=True, db_column='startTime', null=True, max_length=100)),
                ('endtime', models.CharField(blank=True, db_column='endTime', null=True, max_length=100)),
                ('duration', models.CharField(blank=True, db_column='Duration', null=True, max_length=100)),
            ],
            options={
                'db_table': 'WorkLog',
                'managed': False,
            },
        ),
    ]
