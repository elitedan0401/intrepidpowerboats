# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-21 13:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import intrepidboats.apps.boats.fields


class Migration(migrations.Migration):

    dependencies = [
        ('boats', '0030_auto_20170616_0818'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoatLengthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', verbose_name='slug')),
                ('show_image', intrepidboats.apps.boats.fields.BoatImageField(upload_to='boat_images/', verbose_name='show image')),
            ],
            options={
                'verbose_name_plural': 'boat length groups',
                'verbose_name': 'boat length group',
            },
        ),
        migrations.AddField(
            model_name='boat',
            name='length_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='boats', to='boats.BoatLengthGroup', verbose_name='length group'),
        ),
    ]
