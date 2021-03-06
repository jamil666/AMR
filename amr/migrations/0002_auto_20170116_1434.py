# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(help_text='Image file will be stored on /static/images folder', upload_to='C:\\Django\\site_amr/amr/static/images')),
                ('CSS', models.ImageField(help_text='CSS file will be stored on /static/css folder', upload_to='C:\\Django\\site_amr/amr/static/css')),
            ],
        ),
        migrations.DeleteModel(
            name='UploadImage',
        ),
    ]
