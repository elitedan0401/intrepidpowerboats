# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-12 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0026_auto_20170512_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitemetadata',
            name='careers_description',
            field=models.CharField(default='Interested in working for Intrepid? Check out our job listings below and complete the form to send us your information. If you’re a fit, we’ll be in touch!', max_length=1000, verbose_name='All models: Description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitemetadata',
            name='careers_og_description',
            field=models.CharField(default='Interested in working for Intrepid? Check out our job listings below and complete the form to send us your information. If you’re a fit, we’ll be in touch!', max_length=1000, verbose_name='All models: open graph: description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitemetadata',
            name='careers_og_title',
            field=models.CharField(default='Employment at Intrepid - Intrepid Powerboats', max_length=100, verbose_name='All models: open graph: title'),
            preserve_default=False,
        ),
    ]
