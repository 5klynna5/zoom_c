# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('permission_text', models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], blank=True, max_length=3, null=True)),
                ('permission_photo', models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], blank=True, max_length=3, null=True)),
                ('permission_email', models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], blank=True, max_length=3, null=True)),
                ('permission_call', models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], blank=True, max_length=3, null=True)),
                ('permission_mail', models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], blank=True, max_length=3, null=True)),
                ('permission_facebook', models.CharField(choices=[('Yes', 'YES'), ('No', 'NO')], blank=True, max_length=3, null=True)),
                ('contact_pref', models.CharField(choices=[('Facebook', 'FACEBOOK'), ('Email', 'EMAIL'), ('Mail', 'MAIL'), ('Call', 'CALL'), ('Text', 'TEXT')], blank=True, max_length=8, null=True)),
                ('date_updated', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hours',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('date', models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.')),
                ('hours_num', models.PositiveSmallIntegerField()),
                ('volunteer_activity', models.CharField(choices=[('FOOD_SHELF', 'Food Shelf'), ('ZOOM_GALA', 'ZOOM Gala'), ('OTHER', 'Other')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('volunteer_id', models.AutoField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('start_date', models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.')),
                ('organization', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='hours',
            name='volunteer',
            field=models.ForeignKey(to='zoom_vols.Volunteer'),
        ),
        migrations.AddField(
            model_name='contact',
            name='volunteer',
            field=models.ForeignKey(to='zoom_vols.Volunteer'),
        ),
    ]
