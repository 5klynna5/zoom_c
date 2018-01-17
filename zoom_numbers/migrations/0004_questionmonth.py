# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zoom_numbers', '0003_policecalls_num_noise_calls'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionMonth',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('month', models.CharField(choices=[('Jan', 'January'), ('Feb', 'February'), ('Mar', 'March'), ('Apr', 'April'), ('May', 'May'), ('Jun', 'June'), ('Jul', 'July'), ('Aug', 'August'), ('Sep', 'September'), ('Oct', 'October'), ('Nov', 'November'), ('Dec', 'December')], max_length=3)),
                ('year', models.PositiveSmallIntegerField()),
                ('question', models.CharField(max_length=50)),
                ('category_one', models.CharField(max_length=25)),
                ('category_one_count', models.SmallIntegerField()),
                ('category_two', models.CharField(max_length=25)),
                ('category_two_count', models.SmallIntegerField()),
                ('category_three', models.CharField(max_length=25)),
                ('category_three_count', models.SmallIntegerField()),
                ('category_four', models.CharField(max_length=25)),
                ('category_four_count', models.SmallIntegerField()),
            ],
        ),
    ]
