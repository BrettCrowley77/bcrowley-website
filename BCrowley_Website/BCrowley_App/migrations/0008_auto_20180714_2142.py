# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-15 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BCrowley_App', '0007_auto_20180714_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='online_reference',
        ),
        migrations.AlterField(
            model_name='project',
            name='cover_photo',
            field=models.FilePathField(path='/home/brettcrowley77/bcrowley-website/BCrowley_Website/static/img'),
        ),
    ]
