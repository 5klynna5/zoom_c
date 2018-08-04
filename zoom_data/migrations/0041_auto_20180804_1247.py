# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0040_auto_20180804_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('shelter_name', models.CharField(max_length=35)),
                ('shelter_location', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(choices=[('Email', 'EMAIL'), ('Mail', 'MAIL'), ('Call', 'CALL'), ('Text', 'TEXT'), ('Facebook', 'FACEBOOK')], blank=True, max_length=8, null=True),
        ),
    ]
