# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-19 15:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0007_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraUserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchased_boat_info', models.TextField(blank=True, null=True, verbose_name='Purchased boat info')),
                ('details_for_staff', models.TextField(blank=True, null=True, verbose_name='Details for staff')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Extra user information',
                'verbose_name_plural': 'Extra user information',
            },
        ),
    ]
