# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 10:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_auto_20170718_1136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filemodel',
            old_name='file_obj',
            new_name='file',
        ),
    ]
