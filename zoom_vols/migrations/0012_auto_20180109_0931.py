# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_vols', '0011_auto_20180109_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteergroup',
            name='num_volunteers',
            field=models.SmallIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='contact_pref',
            field=models.CharField(blank=True, null=True, choices=[('Text', 'TEXT'), ('Email', 'EMAIL'), ('Mail', 'MAIL'), ('Call', 'CALL'), ('Do Not Contact', 'DO_NOT_CONTACT'), ('Facebook', 'FACEBOOK')], max_length=16),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_call',
            field=models.CharField(blank=True, null=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_email',
            field=models.CharField(blank=True, null=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_facebook',
            field=models.CharField(blank=True, null=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_mail',
            field=models.CharField(blank=True, null=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_photo',
            field=models.CharField(blank=True, null=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_text',
            field=models.CharField(blank=True, null=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3),
        ),
    ]
