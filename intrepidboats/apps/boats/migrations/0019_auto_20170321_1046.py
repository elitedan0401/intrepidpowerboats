# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-21 14:46
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boats', '0018_motorcoloroption_color2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motorcoloroption',
            name='color2',
            field=colorfield.fields.ColorField(default='#FFFFFF', max_length=10),
        ),
    ]
