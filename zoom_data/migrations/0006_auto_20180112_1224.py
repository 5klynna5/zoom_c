# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0005_auto_20180111_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExitInterview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exit_date', models.DateField(blank=True, help_text='Please use the following format: <em>YYYY-MM-DD</em>.', null=True)),
                ('living_next', models.CharField(choices=[('Staying with friend or family', 'FRIEND_FAMILY'), ('Section 8 Housing', 'SECTION_8'), ('Market Rate Housing', 'MARKET_RATE'), ('Other Housing Program', 'OTHER_PROGRAM'), ('Shelter', 'SHELTER'), ('Do not know', 'UNKNOWN'), ('Other', 'OTHER'), ('Prefer not to say', 'PREFER_NOT_SAY')], blank=True, null=True, max_length=15)),
                ('living_next_other', models.CharField(blank=True, null=True, max_length=30)),
                ('goal_one_name', models.CharField(blank=True, null=True, max_length=30)),
                ('goal_one_progress', models.CharField(choices=[('less than 25%', 'less than 25%'), ('25%', '25%'), ('50%', '50%'), ('75%', '75%'), ('100%', '100%')], blank=True, max_length=13, default='less than 25%')),
                ('goal_one_status', models.TextField(blank=True)),
                ('goal_two_name', models.CharField(blank=True, null=True, max_length=30)),
                ('goal_two_progress', models.CharField(choices=[('less than 25%', 'less than 25%'), ('25%', '25%'), ('50%', '50%'), ('75%', '75%'), ('100%', '100%')], blank=True, max_length=13, default='less than 25%')),
                ('goal_two_status', models.TextField(blank=True)),
                ('goals_future', models.TextField(blank=True)),
                ('why_leaving', models.TextField(blank=True)),
                ('most_helpful', models.TextField(blank=True)),
                ('not_helpful', models.TextField(blank=True)),
                ('advice_resident', models.TextField(blank=True)),
                ('advice_staff', models.TextField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='household',
            name='exit_date',
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(choices=[('Email', 'EMAIL'), ('Call', 'CALL'), ('Facebook', 'FACEBOOK'), ('Mail', 'MAIL'), ('Text', 'TEXT')], blank=True, null=True, max_length=8),
        ),
        migrations.AddField(
            model_name='exitinterview',
            name='household',
            field=models.ForeignKey(to='zoom_data.Household'),
        ),
    ]
