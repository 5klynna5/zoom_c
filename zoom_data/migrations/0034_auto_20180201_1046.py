# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0033_auto_20180129_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annual',
            name='employment_status',
            field=models.CharField(null=True, blank=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3),
        ),
        migrations.AlterField(
            model_name='annual',
            name='student_status',
            field=models.CharField(null=True, blank=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(null=True, blank=True, choices=[('Facebook', 'FACEBOOK'), ('Email', 'EMAIL'), ('Call', 'CALL'), ('Text', 'TEXT'), ('Mail', 'MAIL')], max_length=8),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_call',
            field=models.CharField(null=True, blank=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_email',
            field=models.CharField(null=True, blank=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_facebook',
            field=models.CharField(null=True, blank=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_mail',
            field=models.CharField(null=True, blank=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_photo',
            field=models.CharField(null=True, blank=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_text',
            field=models.CharField(null=True, blank=True, choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3),
        ),
        migrations.AlterField(
            model_name='household',
            name='unit_type',
            field=models.CharField(null=True, blank=True, choices=[('SH_ONE_BEDROOM', 'One Bedroom'), ('SH_MARIF', 'MARIF'), ('SH_STUDIO', 'Studio')], max_length=10),
        ),
    ]
