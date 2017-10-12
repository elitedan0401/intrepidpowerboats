# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-24 16:30
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyAreaPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='contact_companyareaplugin', serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='EmployeeProfilePlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='contact_employeeprofileplugin', serialize=False, to='cms.CMSPlugin')),
                ('full_name', models.CharField(max_length=255, verbose_name='full name')),
                ('occupation', models.CharField(max_length=255, verbose_name='occupation')),
                ('phone_number', models.CharField(max_length=255, verbose_name='phone number')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='image')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('first_name', models.CharField(max_length=255, verbose_name='first name')),
                ('last_name', models.CharField(max_length=255, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('phone_number', models.CharField(blank=True, max_length=255, verbose_name='phone number')),
                ('comments', models.TextField(verbose_name='comments')),
                ('inquiry_type', models.CharField(choices=[('I', 'General inquiry'), ('S', 'Sales'), ('B', 'General boat information')], default='I', max_length=1, verbose_name='inquiry type')),
            ],
            options={
                'verbose_name_plural': 'inquiries',
                'verbose_name': 'inquiry',
            },
        ),
        migrations.CreateModel(
            name='JobApplicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('first_name', models.CharField(max_length=255, verbose_name='first name')),
                ('last_name', models.CharField(max_length=255, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('phone_number', models.CharField(blank=True, max_length=255, verbose_name='phone number')),
                ('additional_notes', models.TextField(blank=True, verbose_name='additional notes')),
                ('resume', models.FileField(blank=True, upload_to='applicant_uploads/', verbose_name='resume')),
            ],
            options={
                'verbose_name_plural': 'job applicants',
                'verbose_name': 'job applicant',
            },
        ),
        migrations.CreateModel(
            name='JobDescriptionPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='contact_jobdescriptionplugin', serialize=False, to='cms.CMSPlugin')),
                ('job_title', models.CharField(max_length=50, verbose_name='job title')),
                ('job_description', ckeditor.fields.RichTextField(verbose_name='job description')),
            ],
            options={
                'verbose_name_plural': 'job description plugins',
                'verbose_name': 'job description plugin',
            },
            bases=('cms.cmsplugin',),
        ),
    ]