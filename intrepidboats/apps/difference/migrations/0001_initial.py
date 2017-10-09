# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 15:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestimonialPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='difference_testimonialplugin', serialize=False, to='cms.CMSPlugin')),
                ('title', models.ImageField(upload_to='', verbose_name='Title')),
                ('first_paragraph', models.TextField(verbose_name='First paragraph')),
                ('extra_paragraphs', models.TextField(verbose_name='Extra paragraphs')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
