# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 18:21
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('difference', '0004_auto_20170105_1215'),
    ]

    operations = [
        migrations.CreateModel(
            name='SharedTestimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('first_name', models.CharField(max_length=255, verbose_name='first name')),
                ('last_name', models.CharField(max_length=255, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('message', models.TextField(verbose_name='text')),
                ('approved', models.BooleanField(default=False, verbose_name='approved')),
                ('file', models.FileField(upload_to='shared_testimonials/', verbose_name='file')),
            ],
            options={
                'verbose_name_plural': 'shared testimonials',
                'verbose_name': 'shared testimonial',
            },
        ),
    ]
