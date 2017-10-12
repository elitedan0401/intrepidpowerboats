# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-11 13:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('owners_portal', '0017_remove_boatmanual_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoatManualGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=255)),
                ('user_boat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owners_portal.UserBoat')),
            ],
            options={
                'get_latest_by': 'modified',
                'ordering': ('-modified', '-created'),
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='boatmanual',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='owners_portal.BoatManualGroup'),
            preserve_default=False,
        ),
    ]