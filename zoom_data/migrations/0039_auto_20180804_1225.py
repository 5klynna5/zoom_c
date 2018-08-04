# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_data', '0038_auto_20180804_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='household',
            name='Child_Support_income',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='household',
            name='DWP_income',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='household',
            name='Employment_income',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='household',
            name='Financial_Aid_income',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='household',
            name='GRH_income',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='household',
            name='MFIP_income',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='household',
            name='MHV_income',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='household',
            name='No_income',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='household',
            name='Public_Assistance_income',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='household',
            name='RRH_income',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='household',
            name='SSI_income',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='household',
            name='Section_8_income',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pref',
            field=models.CharField(null=True, blank=True, choices=[('Mail', 'MAIL'), ('Text', 'TEXT'), ('Facebook', 'FACEBOOK'), ('Email', 'EMAIL'), ('Call', 'CALL')], max_length=8),
        ),
    ]
