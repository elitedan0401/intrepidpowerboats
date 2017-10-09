# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-25 18:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('difference', '0007_auto_20170125_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonialplugin',
            name='testimonial',
        ),
        migrations.AddField(
            model_name='testimonialplugin',
            name='testimonial',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='difference.SharedTestimonial'),
            preserve_default=False,
        ),
    ]
