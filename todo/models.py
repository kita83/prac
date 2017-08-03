#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

from django.db import models
from django.utils import timezone


class Task(models.Model):
    task = models.CharField(max_length=200)
    cre_date = models.DateTimeField('date created', auto_now_add=True)
    deadline = models.DateTimeField('deadline_date', blank=True, null=True)
    priority = models.CharField(default=0, max_length=1)

    def is_deadline_recently(self):
        if self.deadline is not None:
            return self.deadline >= timezone.now() - datetime.timedelta(days=7)
        else:
            return None

    def __str__(self):
        return self.task
