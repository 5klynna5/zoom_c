# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_vols', '0013_auto_20180109_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='contact_pref',
            field=models.CharField(choices=[('Mail', 'MAIL'), ('Text', 'TEXT'), ('Facebook', 'FACEBOOK'), ('Email', 'EMAIL'), ('Call', 'CALL'), ('Do Not Contact', 'DO_NOT_CONTACT')], null=True, blank=True, max_length=16),
        ),
    ]
