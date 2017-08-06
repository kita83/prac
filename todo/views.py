#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render
from todo.models import Task
from django.http import HttpResponse, Http404
from datetime import datetime


def index(request):
    if request.POST.get('addTask'):
        data = request.POST.get('addTask')
        d = Task(task=data, cre_date=datetime.now(), deadline=datetime.now(), priority='0')
        d.save()
    postdata = request.POST.getlist('check')
    if request.method == 'POST' and postdata:
        for data in postdata:
            Task.objects.filter(id=data).delete()
    task_list = Task.objects.all()
    context = {'task_list': task_list}
    return render(request, 'todo/index.html', context)


def archive(request):
    return HttpResponse("You're looking archive page.")


def detail(request):
    # task_detail = get_object_or_404(Task, id=row_id)
    return render(request, 'todo/detail.html', {'task_detail', Task.objects.all()})
