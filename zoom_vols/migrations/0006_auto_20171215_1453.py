# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_vols', '0005_auto_20171215_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='contact_pref',
            field=models.CharField(choices=[('Email', 'EMAIL'), ('Call', 'CALL'), ('Mail', 'MAIL'), ('Do Not Contact', 'DO_NOT_CONTACT'), ('Text', 'TEXT'), ('Facebook', 'FACEBOOK')], max_length=16, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='status',
            field=models.CharField(choices=[('Inactive', 'INACTIVE'), ('Active', 'ACTIVE')], max_length=8, null=True, blank=True),
        ),
    ]
