# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0006_auto_20180112_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(null=True, choices=[('Call', 'CALL'), ('Text', 'TEXT'), ('Facebook', 'FACEBOOK'), ('Email', 'EMAIL'), ('Mail', 'MAIL')], blank=True, max_length=8),
        ),
    ]
