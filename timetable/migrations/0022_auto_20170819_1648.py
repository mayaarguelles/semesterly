# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-08-19 21:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0021_auto_20170818_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textbook',
            name='image_url',
            field=models.URLField(max_length=1000, null=True),
        ),
    ]