# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amr', '0021_auto_20170119_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fifthtable',
            name='Column1_Image',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='fifthtable',
            name='Column2_Image',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='fifthtable',
            name='Column3_Image',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='firsttable',
            name='TableImage',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
    ]