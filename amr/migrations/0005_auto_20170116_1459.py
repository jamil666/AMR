# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amr', '0004_auto_20170116_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='Image',
            field=models.ImageField(blank=True, help_text='Image file will be stored on /static/images folder', null=True, upload_to='C:\\Django\\site_amr/amr/static/images'),
        ),
    ]
