# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_vols', '0007_auto_20171218_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hours',
            name='volunteer_activity',
        ),
        migrations.AddField(
            model_name='hours',
            name='volunteer_activity',
            field=models.ForeignKey(null=True, blank=True, to='zoom_vols.Activity'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='contact_pref',
            field=models.CharField(max_length=16, blank=True, choices=[('Mail', 'MAIL'), ('Call', 'CALL'), ('Email', 'EMAIL'), ('Facebook', 'FACEBOOK'), ('Do Not Contact', 'DO_NOT_CONTACT'), ('Text', 'TEXT')], null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_call',
            field=models.CharField(max_length=3, blank=True, choices=[('Yes', 'YES'), ('No', 'NO')], null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_email',
            field=models.CharField(max_length=3, blank=True, choices=[('Yes', 'YES'), ('No', 'NO')], null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_facebook',
            field=models.CharField(max_length=3, blank=True, choices=[('Yes', 'YES'), ('No', 'NO')], null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_mail',
            field=models.CharField(max_length=3, blank=True, choices=[('Yes', 'YES'), ('No', 'NO')], null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_photo',
            field=models.CharField(max_length=3, blank=True, choices=[('Yes', 'YES'), ('No', 'NO')], null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_text',
            field=models.CharField(max_length=3, blank=True, choices=[('Yes', 'YES'), ('No', 'NO')], null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='status',
            field=models.CharField(max_length=8, blank=True, choices=[('Active', 'ACTIVE'), ('Inactive', 'INACTIVE')], null=True),
        ),
    ]
