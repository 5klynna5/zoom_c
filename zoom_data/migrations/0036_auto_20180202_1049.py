# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0035_auto_20180201_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(choices=[('Text', 'TEXT'), ('Call', 'CALL'), ('Mail', 'MAIL'), ('Facebook', 'FACEBOOK'), ('Email', 'EMAIL')], null=True, blank=True, max_length=8),
        ),
    ]
