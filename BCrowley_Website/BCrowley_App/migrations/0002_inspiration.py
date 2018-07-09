# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-09 23:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BCrowley_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inspiration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ins_type', models.CharField(choices=[('QT', 'Quote'), ('SP', 'Speech'), ('CR', 'Creative')], max_length=264)),
                ('id_name', models.CharField(max_length=264)),
                ('title', models.CharField(max_length=264)),
                ('cover_photo', models.URLField(max_length=264)),
                ('online_reference', models.URLField(max_length=264)),
                ('description', models.TextField()),
            ],
        ),
    ]
