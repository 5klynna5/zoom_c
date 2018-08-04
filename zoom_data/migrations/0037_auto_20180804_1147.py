# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0036_auto_20180202_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='household',
            name='previous_location',
            field=models.CharField(blank=True, null=True, choices=[('SHELTER', 'Shelter'), ('DOUBLED_UP', 'Doubled Up'), ('STREET', 'Street Homeless'), ('TRANSITIONAL', 'Transitional Housing'), ('APT_OR_HOUSE', 'Apartment or House'), ('DV_SHELTER', 'DV Shelter')], max_length=12),
        ),
        migrations.AlterField(
            model_name='annual',
            name='employment_status',
            field=models.CharField(blank=True, null=True, choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3),
        ),
        migrations.AlterField(
            model_name='annual',
            name='student_status',
            field=models.CharField(blank=True, null=True, choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(blank=True, null=True, choices=[('Facebook', 'FACEBOOK'), ('Mail', 'MAIL'), ('Email', 'EMAIL'), ('Text', 'TEXT'), ('Call', 'CALL')], max_length=8),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_call',
            field=models.CharField(blank=True, null=True, choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_email',
            field=models.CharField(blank=True, null=True, choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_facebook',
            field=models.CharField(blank=True, null=True, choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_mail',
            field=models.CharField(blank=True, null=True, choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_photo',
            field=models.CharField(blank=True, null=True, choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_text',
            field=models.CharField(blank=True, null=True, choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3),
        ),
    ]
