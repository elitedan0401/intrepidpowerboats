# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-23 18:49
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0016_auto_20170315_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Description'),
        ),
    ]
