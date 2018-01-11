# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_vols', '0010_auto_20180109_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='contact_pref',
            field=models.CharField(blank=True, null=True, choices=[('Email', 'EMAIL'), ('Text', 'TEXT'), ('Call', 'CALL'), ('Mail', 'MAIL'), ('Do Not Contact', 'DO_NOT_CONTACT'), ('Facebook', 'FACEBOOK')], max_length=16),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_call',
            field=models.CharField(blank=True, null=True, choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_email',
            field=models.CharField(blank=True, null=True, choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_facebook',
            field=models.CharField(blank=True, null=True, choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_mail',
            field=models.CharField(blank=True, null=True, choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_photo',
            field=models.CharField(blank=True, null=True, choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_text',
            field=models.CharField(blank=True, null=True, choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3),
        ),
    ]
