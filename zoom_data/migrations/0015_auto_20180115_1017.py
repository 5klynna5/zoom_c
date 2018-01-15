# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0014_auto_20180113_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(null=True, max_length=8, choices=[('Email', 'EMAIL'), ('Call', 'CALL'), ('Facebook', 'FACEBOOK'), ('Text', 'TEXT'), ('Mail', 'MAIL')], blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_call',
            field=models.CharField(null=True, max_length=3, choices=[('No', 'NO'), ('Yes', 'YES')], blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_email',
            field=models.CharField(null=True, max_length=3, choices=[('No', 'NO'), ('Yes', 'YES')], blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_facebook',
            field=models.CharField(null=True, max_length=3, choices=[('No', 'NO'), ('Yes', 'YES')], blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_mail',
            field=models.CharField(null=True, max_length=3, choices=[('No', 'NO'), ('Yes', 'YES')], blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_photo',
            field=models.CharField(null=True, max_length=3, choices=[('No', 'NO'), ('Yes', 'YES')], blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_text',
            field=models.CharField(null=True, max_length=3, choices=[('No', 'NO'), ('Yes', 'YES')], blank=True),
        ),
    ]
