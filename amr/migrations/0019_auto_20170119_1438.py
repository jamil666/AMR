# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amr', '0018_auto_20170119_1126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fifthtable',
            name='Column1_Image',
        ),
        migrations.AddField(
            model_name='fifthtable',
            name='Image',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
    ]