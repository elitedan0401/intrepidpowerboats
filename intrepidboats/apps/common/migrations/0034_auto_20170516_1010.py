# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-16 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0033_auto_20170516_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmspagemetadata',
            name='og_image',
            field=models.ImageField(blank=True, null=True, upload_to='site_metadata/cms/', verbose_name='Open graph: image'),
        ),
    ]
