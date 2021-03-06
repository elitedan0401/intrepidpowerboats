# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-12 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boats', '0028_deckplanhotspot_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deckplanhotspot',
            name='left_percentage',
            field=models.DecimalField(decimal_places=4, max_digits=7, verbose_name='distance from the left border (in %)'),
        ),
        migrations.AlterField(
            model_name='deckplanhotspot',
            name='top_percentage',
            field=models.DecimalField(decimal_places=4, max_digits=7, verbose_name='distance from the top border (in %)'),
        ),
    ]
