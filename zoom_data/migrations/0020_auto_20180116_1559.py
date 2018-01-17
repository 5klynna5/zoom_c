# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0019_auto_20180116_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitysurvey',
            name='why_come_improve',
            field=models.BooleanField(help_text='I needed to improve in this skill area', default=False),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(null=True, choices=[('Call', 'CALL'), ('Text', 'TEXT'), ('Mail', 'MAIL'), ('Email', 'EMAIL'), ('Facebook', 'FACEBOOK')], blank=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_call',
            field=models.CharField(null=True, choices=[('No', 'NO'), ('Yes', 'YES')], blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_email',
            field=models.CharField(null=True, choices=[('No', 'NO'), ('Yes', 'YES')], blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_facebook',
            field=models.CharField(null=True, choices=[('No', 'NO'), ('Yes', 'YES')], blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_mail',
            field=models.CharField(null=True, choices=[('No', 'NO'), ('Yes', 'YES')], blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_photo',
            field=models.CharField(null=True, choices=[('No', 'NO'), ('Yes', 'YES')], blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_text',
            field=models.CharField(null=True, choices=[('No', 'NO'), ('Yes', 'YES')], blank=True, max_length=3),
        ),
    ]
