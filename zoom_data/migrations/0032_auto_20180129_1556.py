# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0031_auto_20180129_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annual',
            name='annual_income',
            field=models.SmallIntegerField(help_text='in U.S. dollars', blank=True),
        ),
        migrations.AlterField(
            model_name='annual',
            name='employment_status',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], null=True, max_length=3, blank=True),
        ),
        migrations.AlterField(
            model_name='annual',
            name='student_status',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], null=True, max_length=3, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(choices=[('Email', 'EMAIL'), ('Call', 'CALL'), ('Text', 'TEXT'), ('Mail', 'MAIL'), ('Facebook', 'FACEBOOK')], null=True, max_length=8, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_call',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], null=True, max_length=3, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_email',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], null=True, max_length=3, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_facebook',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], null=True, max_length=3, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_mail',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], null=True, max_length=3, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_photo',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], null=True, max_length=3, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_text',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], null=True, max_length=3, blank=True),
        ),
    ]
