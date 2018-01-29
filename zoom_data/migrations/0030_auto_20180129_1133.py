# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0029_auto_20180129_1114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exitinterview',
            old_name='exit_date',
            new_name='exit_interview_date',
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(choices=[('Facebook', 'FACEBOOK'), ('Mail', 'MAIL'), ('Text', 'TEXT'), ('Email', 'EMAIL'), ('Call', 'CALL')], null=True, max_length=8, blank=True),
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
