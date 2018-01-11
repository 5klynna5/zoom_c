# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_vols', '0006_auto_20171215_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='contact_pref',
            field=models.CharField(choices=[('Mail', 'MAIL'), ('Call', 'CALL'), ('Facebook', 'FACEBOOK'), ('Text', 'TEXT'), ('Do Not Contact', 'DO_NOT_CONTACT'), ('Email', 'EMAIL')], blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_call',
            field=models.CharField(choices=[('No', 'NO'), ('Yes', 'YES')], blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_email',
            field=models.CharField(choices=[('No', 'NO'), ('Yes', 'YES')], blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_facebook',
            field=models.CharField(choices=[('No', 'NO'), ('Yes', 'YES')], blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_mail',
            field=models.CharField(choices=[('No', 'NO'), ('Yes', 'YES')], blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_photo',
            field=models.CharField(choices=[('No', 'NO'), ('Yes', 'YES')], blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_text',
            field=models.CharField(choices=[('No', 'NO'), ('Yes', 'YES')], blank=True, max_length=3, null=True),
        ),
    ]
