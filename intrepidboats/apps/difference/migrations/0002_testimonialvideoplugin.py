# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 18:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('difference', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestimonialVideoPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='difference_testimonialvideoplugin', serialize=False, to='cms.CMSPlugin')),
                ('movie_url', models.URLField(verbose_name='Movie URL')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
