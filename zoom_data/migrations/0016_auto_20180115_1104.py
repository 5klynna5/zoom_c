# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0015_auto_20180115_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='mailing_address_city',
            field=models.CharField(max_length=15, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='mailing_address_line_one',
            field=models.CharField(max_length=40, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='mailing_address_line_two',
            field=models.CharField(max_length=40, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='mailing_address_state',
            field=models.CharField(max_length=2, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='mailing_address_zip',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(choices=[('Email', 'EMAIL'), ('Facebook', 'FACEBOOK'), ('Mail', 'MAIL'), ('Call', 'CALL'), ('Text', 'TEXT')], max_length=8, blank=True, null=True),
        ),
    ]
