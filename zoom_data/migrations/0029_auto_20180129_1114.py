# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0028_auto_20180119_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='household',
            name='exit_date',
            field=models.DateField(blank=True, null=True, help_text='Please use the following format: <em>YYYY-MM-DD</em>.'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(blank=True, max_length=8, null=True, choices=[('Text', 'TEXT'), ('Facebook', 'FACEBOOK'), ('Mail', 'MAIL'), ('Email', 'EMAIL'), ('Call', 'CALL')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_call',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[('No', 'NO'), ('Yes', 'YES')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_email',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[('No', 'NO'), ('Yes', 'YES')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_facebook',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[('No', 'NO'), ('Yes', 'YES')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_mail',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[('No', 'NO'), ('Yes', 'YES')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_photo',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[('No', 'NO'), ('Yes', 'YES')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_text',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[('No', 'NO'), ('Yes', 'YES')]),
        ),
    ]
