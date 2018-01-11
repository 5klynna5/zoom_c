# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_vols', '0003_auto_20171214_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='contact_pref',
            field=models.CharField(null=True, max_length=16, blank=True, choices=[('Facebook', 'FACEBOOK'), ('Mail', 'MAIL'), ('Do Not Contact', 'DO_NOT_CONTACT'), ('Call', 'CALL'), ('Email', 'EMAIL'), ('Text', 'TEXT')]),
        ),
    ]
