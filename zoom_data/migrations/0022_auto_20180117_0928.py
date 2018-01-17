# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0021_auto_20180116_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitysurvey',
            name='INTERESTING',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='activitysurvey',
            name='NEEDS_IMPROVE',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(null=True, max_length=8, blank=True, choices=[('Text', 'TEXT'), ('Call', 'CALL'), ('Mail', 'MAIL'), ('Facebook', 'FACEBOOK'), ('Email', 'EMAIL')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_call',
            field=models.CharField(null=True, max_length=3, blank=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_email',
            field=models.CharField(null=True, max_length=3, blank=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_facebook',
            field=models.CharField(null=True, max_length=3, blank=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_mail',
            field=models.CharField(null=True, max_length=3, blank=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_photo',
            field=models.CharField(null=True, max_length=3, blank=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_text',
            field=models.CharField(null=True, max_length=3, blank=True, choices=[('Yes', 'YES'), ('No', 'NO')]),
        ),
    ]
