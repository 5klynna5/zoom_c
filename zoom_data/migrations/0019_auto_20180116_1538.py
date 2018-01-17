# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0018_auto_20180115_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivitySurvey',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('survey_complete_date', models.DateField(blank=True, null=True, help_text='Please use the following format: <em>YYYY-MM-DD</em>.')),
                ('activity', models.ForeignKey(to='zoom_data.Activity')),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(blank=True, null=True, choices=[('Facebook', 'FACEBOOK'), ('Mail', 'MAIL'), ('Email', 'EMAIL'), ('Text', 'TEXT'), ('Call', 'CALL')], max_length=8),
        ),
    ]
