# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-13 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners_portal', '0008_sharedvideo_video_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharedvideo',
            name='thumbnail',
            field=models.URLField(blank=True, null=True, verbose_name='thumbnail'),
        ),
    ]
