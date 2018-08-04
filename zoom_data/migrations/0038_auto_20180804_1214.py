# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0037_auto_20180804_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='household',
            name='previous_address',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(max_length=8, null=True, choices=[('Call', 'CALL'), ('Text', 'TEXT'), ('Mail', 'MAIL'), ('Email', 'EMAIL'), ('Facebook', 'FACEBOOK')], blank=True),
        ),
    ]
