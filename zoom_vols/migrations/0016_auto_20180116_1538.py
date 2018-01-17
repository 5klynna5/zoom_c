# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_vols', '0015_auto_20180111_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='contact_pref',
            field=models.CharField(blank=True, null=True, choices=[('Mail', 'MAIL'), ('Text', 'TEXT'), ('Email', 'EMAIL'), ('Facebook', 'FACEBOOK'), ('Do Not Contact', 'DO_NOT_CONTACT'), ('Call', 'CALL')], max_length=16),
        ),
    ]
