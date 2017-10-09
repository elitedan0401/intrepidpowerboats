# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-17 13:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boats', '0025_auto_20170517_0938'),
        ('common', '0035_auto_20170516_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='boats.Video'),
        ),
    ]
