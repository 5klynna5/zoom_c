# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0020_auto_20180116_1559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activitysurvey',
            old_name='why_come_improve',
            new_name='NEEDS_IMPROVE',
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(blank=True, null=True, max_length=8, choices=[('Email', 'EMAIL'), ('Facebook', 'FACEBOOK'), ('Text', 'TEXT'), ('Mail', 'MAIL'), ('Call', 'CALL')]),
        ),
    ]
