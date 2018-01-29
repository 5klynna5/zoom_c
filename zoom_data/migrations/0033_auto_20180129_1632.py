# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0032_auto_20180129_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseNotes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date_notes', models.DateField(null=True, help_text='Enter the date notes were taken. Please use the following format: <em>YYYY-MM-DD</em>.', blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
                ('resident', models.ForeignKey(to='zoom_data.Resident')),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(null=True, max_length=8, choices=[('Email', 'EMAIL'), ('Call', 'CALL'), ('Mail', 'MAIL'), ('Facebook', 'FACEBOOK'), ('Text', 'TEXT')], blank=True),
        ),
    ]
