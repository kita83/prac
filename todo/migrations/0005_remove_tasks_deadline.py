# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 11:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20170730_1738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='deadline',
        ),
    ]
