# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 05:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gardenDiary', '0002_auto_20161121_0515'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='gardenDiary',
            new_name='post',
        ),
    ]
