#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render
from todo.models import Task
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    postdata = request.POST
    if request.method == 'POST' and len(postdata) > 0:
        for data in postdata:
            d = Task.objects.filter(id=data)
            d.delete()
    task_list = Task.objects.all()
    context = {'task_list': task_list}
    return render(request, 'todo/index.html', context)


def archive(request):
    return HttpResponse("You're looking archive page.")


def detail(request, task_id):
    item_list = []
    if request.method == 'POST':
        item_list = request.POST.getlist('check')
    context = {'item_list': item_list}
    # task = get_object_or_404(Task, pk=task_id)

    return render(request, 'todo/detail.html', context)
