# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0030_auto_20180129_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annual',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('self_cert_date', models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.', null=True, blank=True)),
                ('annual_income', models.SmallIntegerField(help_text='in annual dollars', blank=True)),
                ('student_status', models.CharField(choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3, null=True, blank=True)),
                ('employment_status', models.CharField(choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3, null=True, blank=True)),
                ('resident', models.ForeignKey(to='zoom_data.Resident')),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(choices=[('Facebook', 'FACEBOOK'), ('Email', 'EMAIL'), ('Call', 'CALL'), ('Mail', 'MAIL'), ('Text', 'TEXT')], max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_call',
            field=models.CharField(choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_email',
            field=models.CharField(choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_facebook',
            field=models.CharField(choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_mail',
            field=models.CharField(choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_photo',
            field=models.CharField(choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permission_text',
            field=models.CharField(choices=[('No', 'NO'), ('Yes', 'YES')], max_length=3, null=True, blank=True),
        ),
    ]
