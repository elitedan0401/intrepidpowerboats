# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-30 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeprofileplugin',
            name='image',
            field=models.ImageField(blank=True, upload_to='cms/', verbose_name='image'),
        ),
    ]
