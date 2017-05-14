# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0003_portfolioreleases'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('sprintid', models.AutoField(primary_key=True, serialize=False)),
                ('details', models.CharField(blank=True, max_length=100, null=True)),
                ('startdate', models.DateField(blank=True, db_column='startDate', null=True)),
                ('end', models.DateField(blank=True, db_column='End', null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'sprint',
            },
        ),
        migrations.AlterModelTable(
            name='userstory',
            table='userstory',
        ),
    ]
