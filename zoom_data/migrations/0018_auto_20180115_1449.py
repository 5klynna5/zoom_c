# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0017_auto_20180115_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowUp',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('follow_up_date', models.DateField(blank=True, null=True, help_text='Please use the following format: <em>YYYY-MM-DD</em>.')),
                ('apply_goals', models.TextField(blank=True, null=True)),
                ('use_skills', models.TextField(blank=True, null=True)),
                ('compare_before', models.TextField(blank=True, null=True)),
                ('affected_life', models.TextField(blank=True, null=True)),
                ('attendance', models.ForeignKey(to='zoom_data.Attendance')),
            ],
        ),
        migrations.RemoveField(
            model_name='activityfollowup',
            name='attendance',
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(choices=[('Email', 'EMAIL'), ('Call', 'CALL'), ('Facebook', 'FACEBOOK'), ('Text', 'TEXT'), ('Mail', 'MAIL')], max_length=8, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_call',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_email',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_facebook',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_mail',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_photo',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_text',
            field=models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], max_length=3, blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='ActivityFollowUp',
        ),
    ]
