# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-25 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boats', '0009_featureoption_display_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='beam',
            field=models.CharField(max_length=255, verbose_name='beam'),
        ),
    ]
