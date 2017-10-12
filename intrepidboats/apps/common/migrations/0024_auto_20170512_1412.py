# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-12 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0023_auto_20170512_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitemetadata',
            name='description',
            field=models.CharField(default='Intrepid Powerboats creates one of a kind custom powerboats for boat enthusiasts. We are the Industry leading power boat manufacturers.', max_length=500, verbose_name='Description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitemetadata',
            name='og_description',
            field=models.CharField(default='Intrepid Powerboats creates one of a kind custom powerboats for boat enthusiasts. We are the Industry leading power boat manufacturers.', max_length=500, verbose_name='Open graph: description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitemetadata',
            name='og_image',
            field=models.ImageField(blank=True, null=True, upload_to='site_metadata/', verbose_name='Open graph: image'),
        ),
        migrations.AddField(
            model_name='sitemetadata',
            name='og_title',
            field=models.CharField(default='Intrepid Powerboats - Custom Powerboat Manufacturers', max_length=500, verbose_name='Open graph: title'),
            preserve_default=False,
        ),
    ]