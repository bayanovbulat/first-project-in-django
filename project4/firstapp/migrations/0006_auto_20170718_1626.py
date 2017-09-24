# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_auto_20170718_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='filemodel',
            name='number',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='filemodel',
            name='file',
            field=models.FileField(upload_to='firstapp/static/'),
        ),
    ]