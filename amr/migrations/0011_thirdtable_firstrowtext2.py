# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amr', '0010_thirdtable'),
    ]

    operations = [
        migrations.AddField(
            model_name='thirdtable',
            name='FirstRowText2',
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
