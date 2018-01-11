# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_vols', '0004_auto_20171214_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='status',
            field=models.CharField(blank=True, max_length=8, choices=[('Active', 'ACTIVE'), ('Inactive', 'INACTIVE')], null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='contact_pref',
            field=models.CharField(blank=True, max_length=16, choices=[('Do Not Contact', 'DO_NOT_CONTACT'), ('Email', 'EMAIL'), ('Facebook', 'FACEBOOK'), ('Call', 'CALL'), ('Mail', 'MAIL'), ('Text', 'TEXT')], null=True),
        ),
    ]
