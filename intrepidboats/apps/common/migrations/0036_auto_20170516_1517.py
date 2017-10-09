# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-16 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0035_auto_20170516_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmspagemetadata',
            name='og_title',
            field=models.CharField(max_length=500, verbose_name='Open graph: title'),
        ),
        migrations.AlterField(
            model_name='cmspagemetadata',
            name='page_title',
            field=models.CharField(max_length=500, verbose_name='Page title'),
        ),
        migrations.AlterField(
            model_name='sitemetadata',
            name='events_og_title',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Events: open graph: title'),
        ),
        migrations.AlterField(
            model_name='sitemetadata',
            name='owners_portal_og_title',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name="Owner's portal: open graph: title"),
        ),
        migrations.AlterField(
            model_name='sitemetadata',
            name='page_title',
            field=models.CharField(max_length=500, verbose_name='Page title'),
        ),
        migrations.AlterField(
            model_name='sitemetadata',
            name='whats_new_og_title',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name="What's new: open graph: title"),
        ),
    ]
