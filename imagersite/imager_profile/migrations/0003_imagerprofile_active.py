# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_profile', '0002_remove_imagerprofile_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagerprofile',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
