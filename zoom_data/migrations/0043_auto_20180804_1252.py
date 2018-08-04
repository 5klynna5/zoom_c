# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0042_auto_20180804_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(max_length=8, blank=True, null=True, choices=[('Mail', 'MAIL'), ('Call', 'CALL'), ('Facebook', 'FACEBOOK'), ('Text', 'TEXT'), ('Email', 'EMAIL')]),
        ),
        migrations.AlterField(
            model_name='household',
            name='shelter',
            field=models.CharField(help_text='If a shelter was most recent location, please record name of shelter here.', max_length=30, blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Shelter',
        ),
    ]
