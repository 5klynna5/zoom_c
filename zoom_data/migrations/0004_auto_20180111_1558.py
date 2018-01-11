# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0003_auto_20180111_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resident',
            name='resident_exit',
        ),
        migrations.AddField(
            model_name='household',
            name='exit_date',
            field=models.DateField(blank=True, null=True, help_text='Please use the following format: <em>YYYY-MM-DD</em>.'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(max_length=8, blank=True, choices=[('Mail', 'MAIL'), ('Email', 'EMAIL'), ('Call', 'CALL'), ('Text', 'TEXT'), ('Facebook', 'FACEBOOK')], null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_call',
            field=models.CharField(max_length=3, blank=True, choices=[('Yes', 'YES'), ('No', 'NO')], null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_email',
            field=models.CharField(max_length=3, blank=True, choices=[('Yes', 'YES'), ('No', 'NO')], null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_facebook',
            field=models.CharField(max_length=3, blank=True, choices=[('Yes', 'YES'), ('No', 'NO')], null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_mail',
            field=models.CharField(max_length=3, blank=True, choices=[('Yes', 'YES'), ('No', 'NO')], null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_photo',
            field=models.CharField(max_length=3, blank=True, choices=[('Yes', 'YES'), ('No', 'NO')], null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_text',
            field=models.CharField(max_length=3, blank=True, choices=[('Yes', 'YES'), ('No', 'NO')], null=True),
        ),
    ]
