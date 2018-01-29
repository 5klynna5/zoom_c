# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_funds_events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('funder', models.CharField(null=True, blank=True, max_length=20)),
                ('grant_title', models.CharField(null=True, blank=True, max_length=20)),
                ('date_applied', models.DateField(null=True, help_text='Please use the following format: <em>YYYY-MM-DD</em>.', blank=True)),
                ('date_funds_received', models.DateField(null=True, help_text='Please use the following format: <em>YYYY-MM-DD</em>.', blank=True)),
                ('grant_start_date', models.DateField(null=True, help_text='Please use the following format: <em>YYYY-MM-DD</em>.', blank=True)),
                ('grant_end_date', models.DateField(null=True, help_text='Please use the following format: <em>YYYY-MM-DD</em>.', blank=True)),
                ('funding_requirements', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(null=True, help_text='Please use the following format: <em>YYYY-MM-DD</em>.', blank=True),
        ),
    ]
