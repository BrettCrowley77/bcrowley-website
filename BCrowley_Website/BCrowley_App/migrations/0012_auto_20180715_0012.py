# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-15 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BCrowley_App', '0011_auto_20180715_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='cover_photo_local',
            field=models.CharField(blank=True, max_length=264),
        ),
    ]
