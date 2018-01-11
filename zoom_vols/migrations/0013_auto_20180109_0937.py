# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_vols', '0012_auto_20180109_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='contact_pref',
            field=models.CharField(null=True, blank=True, max_length=16, choices=[('Do Not Contact', 'DO_NOT_CONTACT'), ('Mail', 'MAIL'), ('Call', 'CALL'), ('Facebook', 'FACEBOOK'), ('Text', 'TEXT'), ('Email', 'EMAIL')]),
        ),
    ]
