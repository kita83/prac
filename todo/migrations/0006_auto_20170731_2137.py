# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 12:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_remove_tasks_deadline'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tasks',
            new_name='Task',
        ),
    ]
