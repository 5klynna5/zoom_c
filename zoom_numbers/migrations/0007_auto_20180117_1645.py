# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_numbers', '0006_remove_policecalls_num_noise_calls'),
    ]

    operations = [
        migrations.AddField(
            model_name='policecalls',
            name='assault',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='policecalls',
            name='disturbance',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='policecalls',
            name='domestic',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='policecalls',
            name='drug',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='policecalls',
            name='health',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='policecalls',
            name='other',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='policecalls',
            name='theft',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='policecalls',
            name='violence',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
