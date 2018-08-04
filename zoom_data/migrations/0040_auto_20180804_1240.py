# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0039_auto_20180804_1225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='household',
            old_name='previous_location',
            new_name='most_recent_location',
        ),
        migrations.RemoveField(
            model_name='household',
            name='previous_address',
        ),
        migrations.AddField(
            model_name='household',
            name='shelter',
            field=models.CharField(null=True, max_length=25, blank=True, help_text='If a shelter was most recent location, please record name of shelter here.'),
        ),
        migrations.AlterField(
            model_name='annual',
            name='employment_status',
            field=models.CharField(null=True, max_length=3, choices=[('No', 'NO'), ('Yes', 'YES')], blank=True),
        ),
        migrations.AlterField(
            model_name='annual',
            name='student_status',
            field=models.CharField(null=True, max_length=3, choices=[('No', 'NO'), ('Yes', 'YES')], blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(null=True, max_length=8, choices=[('Email', 'EMAIL'), ('Text', 'TEXT'), ('Facebook', 'FACEBOOK'), ('Call', 'CALL'), ('Mail', 'MAIL')], blank=True),
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
