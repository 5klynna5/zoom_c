# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0025_auto_20180117_0939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitysurvey',
            name='how_apply',
        ),
        migrations.AddField(
            model_name='activitysurvey',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='activitysurvey',
            name='confident_after',
            field=models.CharField(blank=True, null=True, max_length=10, choices=[('NOT_AT_ALL', 'Not at all confident'), ('SIGHTLY', 'Slightly confident'), ('SOMEWHAT', 'Somewhat confident'), ('MODERATELY', 'Moderately confident'), ('EXTREMELY', 'Extremely confident')]),
        ),
        migrations.AddField(
            model_name='activitysurvey',
            name='confident_before',
            field=models.CharField(blank=True, null=True, max_length=10, choices=[('NOT_AT_ALL', 'Not at all confident'), ('SIGHTLY', 'Slightly confident'), ('SOMEWHAT', 'Somewhat confident'), ('MODERATELY', 'Moderately confident'), ('EXTREMELY', 'Extremely confident')]),
        ),
        migrations.AddField(
            model_name='activitysurvey',
            name='unit_type',
            field=models.CharField(blank=True, null=True, max_length=10, choices=[('SUPPORTIVE', 'Supportive Housing'), ('MARIF', 'MARIF'), ('STUDIO', 'Studio')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(blank=True, null=True, max_length=8, choices=[('Call', 'CALL'), ('Facebook', 'FACEBOOK'), ('Email', 'EMAIL'), ('Mail', 'MAIL'), ('Text', 'TEXT')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_call',
            field=models.CharField(blank=True, null=True, max_length=3, choices=[('No', 'NO'), ('Yes', 'YES')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_email',
            field=models.CharField(blank=True, null=True, max_length=3, choices=[('No', 'NO'), ('Yes', 'YES')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_facebook',
            field=models.CharField(blank=True, null=True, max_length=3, choices=[('No', 'NO'), ('Yes', 'YES')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_mail',
            field=models.CharField(blank=True, null=True, max_length=3, choices=[('No', 'NO'), ('Yes', 'YES')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_photo',
            field=models.CharField(blank=True, null=True, max_length=3, choices=[('No', 'NO'), ('Yes', 'YES')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_text',
            field=models.CharField(blank=True, null=True, max_length=3, choices=[('No', 'NO'), ('Yes', 'YES')]),
        ),
    ]
