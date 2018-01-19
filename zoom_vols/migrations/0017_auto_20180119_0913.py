# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_vols', '0016_auto_20180116_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='contact_pref',
            field=models.CharField(blank=True, choices=[('Email', 'EMAIL'), ('Facebook', 'FACEBOOK'), ('Text', 'TEXT'), ('Mail', 'MAIL'), ('Do Not Contact', 'DO_NOT_CONTACT'), ('Call', 'CALL')], max_length=16, null=True),
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='interests',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='interests',
            field=models.TextField(blank=True, null=True),
        ),
    ]
