# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-03 12:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import intrepidboats.apps.boats.fields


class Migration(migrations.Migration):

    dependencies = [
        ('boats', '0014_optionalequipment_vimeo_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutTheBoat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', verbose_name='slug')),
                ('brochure', models.FileField(blank=True, null=True, upload_to='boat_brochures/', verbose_name='brochure')),
                ('boat', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='about', to='boats.Boat', verbose_name='boat')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AboutTheBoatImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('image', intrepidboats.apps.boats.fields.BoatImageField(blank=True, null=True, upload_to='boat_images/', verbose_name='image')),
                ('kind', models.CharField(choices=[('EXTERIOR', 'exterior'), ('INTERIOR', 'interior')], max_length=25, verbose_name='kind')),
                ('about_the_boat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='boats.AboutTheBoat', verbose_name='about')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
