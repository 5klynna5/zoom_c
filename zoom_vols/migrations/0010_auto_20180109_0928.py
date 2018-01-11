# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_vols', '0009_auto_20171218_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteerGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('group_org', models.CharField(max_length=25, blank=True, null=True)),
                ('date', models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.')),
                ('hours_num', models.PositiveSmallIntegerField()),
                ('volunteer_activity', models.ForeignKey(to='zoom_vols.Activity', null=True, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='contact_pref',
            field=models.CharField(choices=[('Mail', 'MAIL'), ('Email', 'EMAIL'), ('Facebook', 'FACEBOOK'), ('Text', 'TEXT'), ('Call', 'CALL'), ('Do Not Contact', 'DO_NOT_CONTACT')], max_length=16, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_call',
            field=models.CharField(choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_email',
            field=models.CharField(choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_facebook',
            field=models.CharField(choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_mail',
            field=models.CharField(choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_photo',
            field=models.CharField(choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='permission_text',
            field=models.CharField(choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3, blank=True, null=True),
        ),
    ]
