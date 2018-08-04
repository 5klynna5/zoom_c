# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0043_auto_20180804_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annual',
            name='employment_status',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='annual',
            name='student_status',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='move_in_date',
            field=models.DateField(default='1999-09-09', help_text='Please use the following format: <em>YYYY-MM-DD</em>.'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(choices=[('Facebook', 'FACEBOOK'), ('Call', 'CALL'), ('Text', 'TEXT'), ('Mail', 'MAIL'), ('Email', 'EMAIL')], max_length=8, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_call',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_email',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_facebook',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_mail',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_photo',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_text',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='household',
            name='move_in_date',
            field=models.DateField(default='1999-09-09', help_text='Please use the following format: <em>YYYY-MM-DD</em>.'),
        ),
    ]
