# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-07 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_type', models.CharField(choices=[('BK', 'Book'), ('MV', 'Movie'), ('MS', 'Music'), ('AT', 'Article')], max_length=264)),
                ('id_name', models.CharField(max_length=264)),
                ('title', models.CharField(max_length=264)),
                ('author', models.CharField(max_length=264)),
                ('cover_photo', models.URLField(max_length=264)),
                ('online_reference', models.URLField(max_length=264)),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('review', models.TextField()),
            ],
        ),
    ]
