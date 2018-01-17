# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_numbers', '0004_questionmonth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policecalls',
            name='num_noise_calls',
            field=models.SmallIntegerField(default=0),
        ),
    ]
