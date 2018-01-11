# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('activity_name', models.CharField(max_length=25)),
                ('skill_area', models.CharField(null=True, choices=[('FINANCE', 'Finance'), ('PARENTING', 'Parenting'), ('EMPLOYMENT', 'Employment'), ('FITNESS', 'Fitness')], blank=True, max_length=15)),
                ('month', models.CharField(null=True, choices=[('Jan', 'January'), ('Feb', 'February'), ('Mar', 'March'), ('Apr', 'April'), ('May', 'May'), ('Jun', 'June'), ('Jul', 'July'), ('Aug', 'August'), ('Sep', 'September'), ('Oct', 'October'), ('Nov', 'November'), ('Dec', 'December')], blank=True, max_length=3)),
                ('year', models.PositiveSmallIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('complete_date', models.DateField(null=True, blank=True)),
                ('activity', models.ForeignKey(to='zoom_data.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('first_name', models.CharField(null=True, blank=True, max_length=15)),
                ('last_name', models.CharField(null=True, blank=True, max_length=15)),
                ('dob', models.DateField(null=True, blank=True)),
                ('gender', models.CharField(null=True, choices=[('FEMALE', 'Female'), ('MALE', 'Male'), ('ALT', 'Another gender')], blank=True, max_length=6)),
                ('race', models.CharField(null=True, choices=[('AFRICAN_AMERICAN', 'African American'), ('WHITE', 'White'), ('MULTIRACIAL', 'Multiracial'), ('AMER_INDIAN', 'American Indian'), ('PAC_ISLANDER', 'Native Hawaiian or Pacific Islander'), ('ASIAN_AMERICAN', 'Asian American')], blank=True, max_length=16)),
                ('ethnicity', models.CharField(null=True, choices=[('HISPANIC', 'Hispanic'), ('NON-HISPANIC', 'Non-Hispanic')], blank=True, max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='ChildAttendance',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('complete_date', models.DateField(null=True, blank=True)),
                ('activity', models.ForeignKey(to='zoom_data.Activity')),
                ('child', models.ForeignKey(to='zoom_data.Child')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('resident_phone', models.CharField(null=True, blank=True, max_length=10)),
                ('resident_email', models.EmailField(null=True, blank=True, max_length=254)),
                ('permission_text', models.CharField(null=True, choices=[('Yes', 'YES'), ('No', 'NO')], blank=True, max_length=3)),
                ('permission_photo', models.CharField(null=True, choices=[('Yes', 'YES'), ('No', 'NO')], blank=True, max_length=3)),
                ('permission_email', models.CharField(null=True, choices=[('Yes', 'YES'), ('No', 'NO')], blank=True, max_length=3)),
                ('permission_call', models.CharField(null=True, choices=[('Yes', 'YES'), ('No', 'NO')], blank=True, max_length=3)),
                ('permission_mail', models.CharField(null=True, choices=[('Yes', 'YES'), ('No', 'NO')], blank=True, max_length=3)),
                ('permission_facebook', models.CharField(null=True, choices=[('Yes', 'YES'), ('No', 'NO')], blank=True, max_length=3)),
                ('contact_pref', models.CharField(null=True, choices=[('Mail', 'MAIL'), ('Facebook', 'FACEBOOK'), ('Text', 'TEXT'), ('Email', 'EMAIL'), ('Call', 'CALL')], blank=True, max_length=8)),
                ('date_updated', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('goal_name', models.CharField(max_length=100)),
                ('goal_date', models.DateField(null=True, blank=True)),
                ('goal_explain', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Household',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('household_name', models.CharField(null=True, blank=True, max_length=20)),
                ('unit_num', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('unit_type', models.CharField(null=True, choices=[('SUPPORTIVE', 'Supportive Housing'), ('MARIF', 'MARIF'), ('STUDIO', 'Studio')], blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date_progress', models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.')),
                ('percent_progress', models.CharField(choices=[('less than 25%', 'less than 25%'), ('25%', '25%'), ('50%', '50%'), ('75%', '75%'), ('100%', '100%')], default='less than 25%', blank=True, max_length=13)),
                ('notes_progress', models.TextField(blank=True)),
                ('goal', models.ForeignKey(to='zoom_data.Goal')),
            ],
        ),
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('resident_id', models.AutoField(serialize=False, primary_key=True)),
                ('resident_first_name', models.CharField(max_length=20)),
                ('resident_last_name', models.CharField(max_length=20)),
                ('resident_move_in', models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.')),
                ('gender', models.CharField(null=True, choices=[('FEMALE', 'Female'), ('MALE', 'Male'), ('ALT', 'Another gender')], blank=True, max_length=6)),
                ('race', models.CharField(null=True, choices=[('AFRICAN_AMERICAN', 'African American'), ('WHITE', 'White'), ('MULTIRACIAL', 'Multiracial'), ('AMER_INDIAN', 'American Indian'), ('PAC_ISLANDER', 'Native Hawaiian or Pacific Islander'), ('ASIAN_AMERICAN', 'Asian American')], blank=True, max_length=16)),
                ('ethnicity', models.CharField(null=True, choices=[('HISPANIC', 'Hispanic'), ('NON-HISPANIC', 'Non-Hispanic')], blank=True, max_length=12)),
                ('health_ins', models.CharField(null=True, choices=[('NONE', 'None'), ('PRIVATE', 'Private'), ('MEDICAID', 'Medicaid'), ('OTHER', 'Other Insurance')], blank=True, max_length=8)),
                ('resident_exit', models.DateField(null=True, help_text='Please use the following format: <em>YYYY-MM-DD</em>.', blank=True)),
                ('household', models.ForeignKey(null=True, to='zoom_data.Household', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='goal',
            name='goal_resident',
            field=models.ForeignKey(to='zoom_data.Resident'),
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_resident',
            field=models.ForeignKey(to='zoom_data.Resident'),
        ),
        migrations.AddField(
            model_name='child',
            name='household',
            field=models.ForeignKey(null=True, to='zoom_data.Household', blank=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='resident',
            field=models.ForeignKey(to='zoom_data.Resident'),
        ),
        migrations.AddField(
            model_name='activity',
            name='children',
            field=models.ManyToManyField(through='zoom_data.ChildAttendance', to='zoom_data.Child'),
        ),
        migrations.AddField(
            model_name='activity',
            name='members',
            field=models.ManyToManyField(through='zoom_data.Attendance', to='zoom_data.Resident'),
        ),
    ]
