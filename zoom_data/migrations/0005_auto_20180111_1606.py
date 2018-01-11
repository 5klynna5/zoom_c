# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0004_auto_20180111_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(blank=True, null=True, choices=[('Mail', 'MAIL'), ('Text', 'TEXT'), ('Email', 'EMAIL'), ('Call', 'CALL'), ('Facebook', 'FACEBOOK')], max_length=8),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_call',
            field=models.CharField(blank=True, null=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_email',
            field=models.CharField(blank=True, null=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_facebook',
            field=models.CharField(blank=True, null=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_mail',
            field=models.CharField(blank=True, null=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_photo',
            field=models.CharField(blank=True, null=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_text',
            field=models.CharField(blank=True, null=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3),
        ),
    ]
