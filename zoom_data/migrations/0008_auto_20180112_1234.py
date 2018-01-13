# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0007_auto_20180112_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(blank=True, max_length=8, null=True, choices=[('Email', 'EMAIL'), ('Facebook', 'FACEBOOK'), ('Mail', 'MAIL'), ('Text', 'TEXT'), ('Call', 'CALL')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_call',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_email',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_facebook',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_mail',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_photo',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_text',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
    ]
