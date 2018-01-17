# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_numbers', '0005_auto_20180117_1105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='policecalls',
            name='num_noise_calls',
        ),
    ]
