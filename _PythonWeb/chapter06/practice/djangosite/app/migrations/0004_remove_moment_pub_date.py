﻿# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-24 05:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160224_0447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moment',
            name='pub_date',
        ),
    ]