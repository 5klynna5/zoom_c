# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_funds_events', '0002_auto_20180129_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='grant',
            name='amount',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
    ]
