# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-27 13:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('owners_portal', '0012_auto_20170316_0920'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='sharedpicture',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('base_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='sharedvideo',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('base_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='sharedvideo',
            name='video_external_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='video external url'),
        ),
    ]
