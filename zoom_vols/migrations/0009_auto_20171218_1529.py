# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_vols', '0008_auto_20171218_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='contact_pref',
            field=models.CharField(max_length=16, null=True, blank=True, choices=[('Facebook', 'FACEBOOK'), ('Text', 'TEXT'), ('Call', 'CALL'), ('Do Not Contact', 'DO_NOT_CONTACT'), ('Mail', 'MAIL'), ('Email', 'EMAIL')]),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='status',
            field=models.CharField(max_length=8, null=True, blank=True, choices=[('Inactive', 'INACTIVE'), ('Active', 'ACTIVE')]),
        ),
    ]
