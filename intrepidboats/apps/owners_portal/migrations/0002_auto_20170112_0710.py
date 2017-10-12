# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 12:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owners_portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sharedvideo',
            options={'verbose_name': 'shared video', 'verbose_name_plural': 'shared videos'},
        ),
        migrations.AlterField(
            model_name='sharedvideo',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='approved'),
        ),
        migrations.AlterField(
            model_name='sharedvideo',
            name='complete_uri',
            field=models.CharField(max_length=610, verbose_name='complete uri'),
        ),
        migrations.AlterField(
            model_name='sharedvideo',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='completed'),
        ),
        migrations.AlterField(
            model_name='sharedvideo',
            name='ticket_id',
            field=models.CharField(max_length=610, verbose_name='ticket id'),
        ),
        migrations.AlterField(
            model_name='sharedvideo',
            name='upload_link_secure',
            field=models.CharField(max_length=610, verbose_name='upload link secure'),
        ),
        migrations.AlterField(
            model_name='sharedvideo',
            name='uploader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shared_videos', to=settings.AUTH_USER_MODEL, verbose_name='uploader'),
        ),
        migrations.AlterField(
            model_name='sharedvideo',
            name='uri',
            field=models.CharField(max_length=255, verbose_name='uri'),
        ),
        migrations.AlterField(
            model_name='sharedvideo',
            name='vimeo_user',
            field=models.TextField(verbose_name='vimeo user'),
        ),
    ]