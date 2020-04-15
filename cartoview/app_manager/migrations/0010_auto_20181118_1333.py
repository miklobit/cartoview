# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-18 13:33
from __future__ import unicode_literals

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('app_manager', '0009_auto_20180920_1659'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='appinstance',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('base_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RenameField(
            model_name='appinstance',
            old_name='map',
            new_name='related_map',
        ),
    ]
