# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_vols', '0018_auto_20180119_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='contact_pref',
            field=models.CharField(null=True, choices=[('Call', 'CALL'), ('Email', 'EMAIL'), ('Facebook', 'FACEBOOK'), ('Text', 'TEXT'), ('Mail', 'MAIL'), ('Do Not Contact', 'DO_NOT_CONTACT')], max_length=16, blank=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='status',
            field=models.CharField(null=True, choices=[('Active', 'ACTIVE'), ('Inactive', 'INACTIVE')], max_length=8, blank=True),
        ),
    ]
