# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 15:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import intrepidboats.apps.boats.fields


class Migration(migrations.Migration):

    dependencies = [
        ('boats', '0003_auto_20161226_1044'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoatModelGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', verbose_name='slug')),
                ('show_image', intrepidboats.apps.boats.fields.BoatImageField(blank=True, null=True, upload_to='boat_images/', verbose_name='show image')),
            ],
            options={
                'verbose_name': 'boat model group',
                'verbose_name_plural': 'boat model groups',
            },
        ),
        migrations.AlterModelOptions(
            name='boat',
            options={'verbose_name': 'boat model', 'verbose_name_plural': 'boat models'},
        ),
        migrations.AlterModelOptions(
            name='motor',
            options={'verbose_name': 'motor'},
        ),
        migrations.AlterModelOptions(
            name='motorinboat',
            options={'verbose_name': 'motor in boat'},
        ),
        migrations.AlterField(
            model_name='boat',
            name='base',
            field=intrepidboats.apps.boats.fields.BoatImageField(blank=True, null=True, upload_to='boat_images/', verbose_name='base'),
        ),
        migrations.AlterField(
            model_name='boat',
            name='boot_stripe',
            field=intrepidboats.apps.boats.fields.BoatImageField(blank=True, null=True, upload_to='boat_images/', verbose_name='boot stripe'),
        ),
        migrations.AlterField(
            model_name='boat',
            name='boot_stripe_accent',
            field=intrepidboats.apps.boats.fields.BoatImageField(blank=True, null=True, upload_to='boat_images/', verbose_name='boot stripe accent'),
        ),
        migrations.AlterField(
            model_name='boat',
            name='hull',
            field=intrepidboats.apps.boats.fields.BoatImageField(blank=True, null=True, upload_to='boat_images/', verbose_name='hull'),
        ),
        migrations.AlterField(
            model_name='boat',
            name='sheer_stripe',
            field=intrepidboats.apps.boats.fields.BoatImageField(blank=True, null=True, upload_to='boat_images/', verbose_name='sheer stripe'),
        ),
        migrations.AlterField(
            model_name='boat',
            name='sheer_stripe_accent',
            field=intrepidboats.apps.boats.fields.BoatImageField(blank=True, null=True, upload_to='boat_images/', verbose_name='sheer stripe accent'),
        ),
        migrations.AlterField(
            model_name='boat',
            name='show_image',
            field=intrepidboats.apps.boats.fields.BoatImageField(blank=True, null=True, upload_to='boat_images/', verbose_name='show image'),
        ),
        migrations.AlterField(
            model_name='motor',
            name='image',
            field=intrepidboats.apps.boats.fields.BoatImageField(blank=True, null=True, upload_to='boat_images/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='motorinboat',
            name='boat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='motors', to='boats.Boat', verbose_name='boat'),
        ),
        migrations.AlterField(
            model_name='motorinboat',
            name='image',
            field=intrepidboats.apps.boats.fields.BoatImageField(blank=True, null=True, upload_to='boat_images/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='motorinboat',
            name='motor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boats.Motor', verbose_name='motor'),
        ),
        migrations.AddField(
            model_name='boat',
            name='model_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='boat_models', to='boats.BoatModelGroup', verbose_name='model group'),
        ),
    ]