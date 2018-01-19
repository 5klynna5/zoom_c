# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0027_auto_20180119_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(null=True, choices=[('Facebook', 'FACEBOOK'), ('Mail', 'MAIL'), ('Call', 'CALL'), ('Email', 'EMAIL'), ('Text', 'TEXT')], max_length=8, blank=True),
        ),
    ]
