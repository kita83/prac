# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 08:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='importance',
        ),
        migrations.AddField(
            model_name='tasks',
            name='priority',
            field=models.CharField(default=0, max_length=1),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='deadline',
            field=models.DateTimeField(blank=True, verbose_name='deadline_date'),
        ),
    ]