# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-11 14:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owners_portal', '0019_move_boat_reference_to_manual_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boatmanual',
            name='user_boat',
        ),
    ]