# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gardenDiary', '0005_post_badge'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='post',
            name='badge',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]
