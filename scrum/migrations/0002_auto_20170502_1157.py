# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfoliolables',
            fields=[
                ('portfoliolablesid', models.AutoField(db_column='portfolioLablesid', primary_key=True, serialize=False)),
                ('label', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'PortfoliLables',
            },
        ),
        migrations.CreateModel(
            name='PortfolioLinksLabel',
            fields=[
                ('portfolioLinkslabelid', models.AutoField(db_column='portfoliolinkslabelid', primary_key=True, serialize=False)),
                ('label', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.CharField(blank=True, db_column='Url', max_length=100, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'portfoliolinkslabelid',
            },
        ),
        migrations.AlterModelTable(
            name='portfoliolinks',
            table='PortfolioLinks',
        ),
        migrations.AlterModelTable(
            name='tasklinkslabel',
            table='tasklinkslabel',
        ),
    ]