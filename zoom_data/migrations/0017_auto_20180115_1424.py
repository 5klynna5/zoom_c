# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0016_auto_20180115_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityFollowUp',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('follow_up_date', models.DateField(null=True, help_text='Please use the following format: <em>YYYY-MM-DD</em>.', blank=True)),
                ('apply_goals', models.TextField(null=True, blank=True)),
                ('use_skills', models.TextField(null=True, blank=True)),
                ('compare_before', models.TextField(null=True, blank=True)),
                ('affected_life', models.TextField(null=True, blank=True)),
                ('attendance', models.ForeignKey(to='zoom_data.Attendance')),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(blank=True, choices=[('Call', 'CALL'), ('Facebook', 'FACEBOOK'), ('Email', 'EMAIL'), ('Mail', 'MAIL'), ('Text', 'TEXT')], null=True, max_length=8),
        ),
    ]
