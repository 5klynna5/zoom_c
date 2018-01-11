# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_vols', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('activity', models.CharField(max_length=15, choices=[('ZOOM_GALA', 'ZOOM Gala'), ('FOOD_SHELF', 'Food Shelf'), ('OTHER', 'Other')])),
            ],
        ),
        migrations.RemoveField(
            model_name='contact',
            name='volunteer',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='contact_pref',
            field=models.CharField(blank=True, null=True, max_length=8, choices=[('Text', 'TEXT'), ('Facebook', 'FACEBOOK'), ('Email', 'EMAIL'), ('Call', 'CALL'), ('Mail', 'MAIL')]),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='date_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='email',
            field=models.EmailField(blank=True, null=True, max_length=254),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='permission_call',
            field=models.CharField(blank=True, null=True, max_length=3, choices=[('No', 'NO'), ('Yes', 'YES')]),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='permission_email',
            field=models.CharField(blank=True, null=True, max_length=3, choices=[('No', 'NO'), ('Yes', 'YES')]),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='permission_facebook',
            field=models.CharField(blank=True, null=True, max_length=3, choices=[('No', 'NO'), ('Yes', 'YES')]),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='permission_mail',
            field=models.CharField(blank=True, null=True, max_length=3, choices=[('No', 'NO'), ('Yes', 'YES')]),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='permission_photo',
            field=models.CharField(blank=True, null=True, max_length=3, choices=[('No', 'NO'), ('Yes', 'YES')]),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='permission_text',
            field=models.CharField(blank=True, null=True, max_length=3, choices=[('No', 'NO'), ('Yes', 'YES')]),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='phone',
            field=models.CharField(blank=True, null=True, max_length=10),
        ),
        migrations.RemoveField(
            model_name='hours',
            name='volunteer_activity',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='interests',
            field=models.ManyToManyField(to='zoom_vols.Activity'),
        ),
        migrations.AddField(
            model_name='hours',
            name='volunteer_activity',
            field=models.ManyToManyField(to='zoom_vols.Activity'),
        ),
    ]
