# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-05-19 03:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0016_course_same_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='same_course',
            new_name='same_as',
        ),
    ]
