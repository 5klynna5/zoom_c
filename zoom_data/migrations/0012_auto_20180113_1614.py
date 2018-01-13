# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0011_auto_20180113_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(blank=True, null=True, max_length=8, choices=[('Email', 'EMAIL'), ('Call', 'CALL'), ('Facebook', 'FACEBOOK'), ('Mail', 'MAIL'), ('Text', 'TEXT')]),
        ),
        migrations.AlterField(
            model_name='resident',
            name='household',
            field=models.ForeignKey(default=2, to='zoom_data.Household'),
            preserve_default=False,
        ),
    ]
