# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_vols', '0019_auto_20180119_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='contact_pref',
            field=models.CharField(null=True, blank=True, choices=[('Facebook', 'FACEBOOK'), ('Mail', 'MAIL'), ('Call', 'CALL'), ('Text', 'TEXT'), ('Email', 'EMAIL'), ('Do Not Contact', 'DO_NOT_CONTACT')], max_length=16),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_call',
            field=models.CharField(null=True, blank=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_email',
            field=models.CharField(null=True, blank=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_facebook',
            field=models.CharField(null=True, blank=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_mail',
            field=models.CharField(null=True, blank=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_photo',
            field=models.CharField(null=True, blank=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_text',
            field=models.CharField(null=True, blank=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='status',
            field=models.CharField(null=True, blank=True, choices=[('Inactive', 'INACTIVE'), ('Active', 'ACTIVE')], max_length=8),
        ),
    ]
