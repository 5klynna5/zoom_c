# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0008_auto_20180112_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(blank=True, choices=[('Call', 'CALL'), ('Facebook', 'FACEBOOK'), ('Mail', 'MAIL'), ('Email', 'EMAIL'), ('Text', 'TEXT')], null=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_call',
            field=models.CharField(blank=True, choices=[('No', 'NO'), ('Yes', 'YES')], null=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_email',
            field=models.CharField(blank=True, choices=[('No', 'NO'), ('Yes', 'YES')], null=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_facebook',
            field=models.CharField(blank=True, choices=[('No', 'NO'), ('Yes', 'YES')], null=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_mail',
            field=models.CharField(blank=True, choices=[('No', 'NO'), ('Yes', 'YES')], null=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_photo',
            field=models.CharField(blank=True, choices=[('No', 'NO'), ('Yes', 'YES')], null=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_text',
            field=models.CharField(blank=True, choices=[('No', 'NO'), ('Yes', 'YES')], null=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='exitinterview',
            name='living_next',
            field=models.CharField(blank=True, choices=[('FRIEND_FAMILY', 'Staying with friend or family'), ('SECTION_8', 'Section 8 Housing'), ('MARKET_RATE', 'Market Rate Housing'), ('OTHER_PROGRAM', 'Other Housing Program'), ('SHELTER', 'Shelter'), ('UNKNOWN', 'Do not know'), ('OTHER', 'Other'), ('PREFER_NOT_SAY', 'Prefer not to say')], null=True, max_length=15),
        ),
    ]
