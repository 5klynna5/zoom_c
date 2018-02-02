# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_vols', '0020_auto_20180201_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='contact_pref',
            field=models.CharField(choices=[('Mail', 'MAIL'), ('Facebook', 'FACEBOOK'), ('Call', 'CALL'), ('Do Not Contact', 'DO_NOT_CONTACT'), ('Email', 'EMAIL'), ('Text', 'TEXT')], null=True, blank=True, max_length=16),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='status',
            field=models.CharField(choices=[('Active', 'ACTIVE'), ('Inactive', 'INACTIVE')], null=True, blank=True, max_length=8),
        ),
    ]
