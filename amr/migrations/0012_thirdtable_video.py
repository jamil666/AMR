# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 05:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amr', '0011_thirdtable_firstrowtext2'),
    ]

    operations = [
        migrations.AddField(
            model_name='thirdtable',
            name='Video',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
