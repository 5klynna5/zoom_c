# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0013_auto_20180113_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(max_length=8, null=True, blank=True, choices=[('Facebook', 'FACEBOOK'), ('Text', 'TEXT'), ('Email', 'EMAIL'), ('Mail', 'MAIL'), ('Call', 'CALL')]),
        ),
    ]
