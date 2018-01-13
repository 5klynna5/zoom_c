# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0009_auto_20180112_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='dob',
            field=models.DateField(null=True, help_text='Please use the following format: <em>YYYY-MM-DD</em>.', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(choices=[('Text', 'TEXT'), ('Facebook', 'FACEBOOK'), ('Call', 'CALL'), ('Mail', 'MAIL'), ('Email', 'EMAIL')], null=True, max_length=8, blank=True),
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
