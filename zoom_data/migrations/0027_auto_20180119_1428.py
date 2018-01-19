# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0026_auto_20180117_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='move_in_date',
            field=models.DateField(null=True, blank=True, help_text='Please use the following format: <em>YYYY-MM-DD</em>.'),
        ),
        migrations.AddField(
            model_name='household',
            name='move_in_date',
            field=models.DateField(null=True, blank=True, help_text='Please use the following format: <em>YYYY-MM-DD</em>.'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(max_length=8, choices=[('Email', 'EMAIL'), ('Facebook', 'FACEBOOK'), ('Text', 'TEXT'), ('Call', 'CALL'), ('Mail', 'MAIL')], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_call',
            field=models.CharField(max_length=3, choices=[('Yes', 'YES'), ('No', 'NO')], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_email',
            field=models.CharField(max_length=3, choices=[('Yes', 'YES'), ('No', 'NO')], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_facebook',
            field=models.CharField(max_length=3, choices=[('Yes', 'YES'), ('No', 'NO')], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_mail',
            field=models.CharField(max_length=3, choices=[('Yes', 'YES'), ('No', 'NO')], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_photo',
            field=models.CharField(max_length=3, choices=[('Yes', 'YES'), ('No', 'NO')], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_text',
            field=models.CharField(max_length=3, choices=[('Yes', 'YES'), ('No', 'NO')], blank=True, null=True),
        ),
    ]
