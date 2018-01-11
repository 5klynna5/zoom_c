# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_vols', '0002_auto_20171214_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity',
            field=models.CharField(max_length=15, choices=[('FOOD_SHELF', 'Food Shelf'), ('ZOOM_GALA', 'ZOOM Gala'), ('OTHER', 'Other')]),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='contact_pref',
            field=models.CharField(max_length=16, blank=True, null=True, choices=[('Text', 'TEXT'), ('Mail', 'MAIL'), ('Call', 'CALL'), ('Email', 'EMAIL'), ('Do Not Contact', 'DO_NOT_CONTACT'), ('Facebook', 'FACEBOOK')]),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_call',
            field=models.CharField(max_length=3, blank=True, null=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_email',
            field=models.CharField(max_length=3, blank=True, null=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_facebook',
            field=models.CharField(max_length=3, blank=True, null=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_mail',
            field=models.CharField(max_length=3, blank=True, null=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_photo',
            field=models.CharField(max_length=3, blank=True, null=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_text',
            field=models.CharField(max_length=3, blank=True, null=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
    ]
