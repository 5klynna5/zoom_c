# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0034_auto_20180201_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(blank=True, choices=[('Mail', 'MAIL'), ('Call', 'CALL'), ('Facebook', 'FACEBOOK'), ('Email', 'EMAIL'), ('Text', 'TEXT')], max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='household',
            name='unit_type',
            field=models.CharField(blank=True, choices=[('SH_ONE_BEDROOM', 'One Bedroom'), ('SH_MARIF', 'MARIF'), ('SH_STUDIO', 'Studio')], max_length=14, null=True),
        ),
    ]
