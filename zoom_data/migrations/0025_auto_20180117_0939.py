# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0024_auto_20180117_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitysurvey',
            name='how_apply',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='activitysurvey',
            name='knowledge_after',
            field=models.CharField(choices=[('NO', 'No knowledge'), ('A_LITTLE', 'A little knowledge'), ('SOME', 'Some knowledge'), ('A_LOT', 'A lot of knowledge'), ('ALL', 'All the knowledge I need')], blank=True, null=True, max_length=8),
        ),
        migrations.AddField(
            model_name='activitysurvey',
            name='knowledge_before',
            field=models.CharField(choices=[('NO', 'No knowledge'), ('A_LITTLE', 'A little knowledge'), ('SOME', 'Some knowledge'), ('A_LOT', 'A lot of knowledge'), ('ALL', 'All the knowledge I need')], blank=True, null=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(choices=[('Mail', 'MAIL'), ('Call', 'CALL'), ('Facebook', 'FACEBOOK'), ('Text', 'TEXT'), ('Email', 'EMAIL')], blank=True, null=True, max_length=8),
        ),
    ]
