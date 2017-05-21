# coding=utf-8
from __future__ import unicode_literals
from django.urls import reverse
from django.db import models



class Team(models.Model):
    teamid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return   self.title

    class Meta:
        managed = False
        db_table = 'Team'


class ResourceType(models.Model):
    resourcetypeid = models.AutoField(db_column='resourceTypeid', primary_key=True)  # Field name made lowercase.
    description = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return   self.description
    class Meta:
        managed = False
        db_table = 'ResourceType'

class Resource(models.Model):
    resourceid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    resourcetypeid = models.ForeignKey('Resourcetype', models.DO_NOTHING, db_column='resourcetypeid')  # Field name made lowercase.
    teamid = models.ForeignKey('team', models.DO_NOTHING, db_column='teamid')  # Field name made lowercase.
    active = models.IntegerField()


    def __str__(self):
        return   self.name
    class Meta:
        managed = False
        db_table = 'Resource'


class TeamResource(models.Model):
    resourceid = models.ForeignKey(Resource, models.DO_NOTHING, db_column='resourceid', primary_key=True)
    teamid = models.ForeignKey(Team, models.DO_NOTHING, db_column='teamid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'TeamResource'
        unique_together = (('resourceid', 'teamid'),)

    class Meta:
        managed = False
        db_table = 'sprint'

