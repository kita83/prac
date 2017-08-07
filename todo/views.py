#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render
from todo.models import Task
from django.http import HttpResponse
from datetime import datetime
from .forms import MyForm


def index(request):
    if request.method == 'POST':
        # 追加
        if request.POST.get('addTask'):
            data = request.POST.get('addTask')
            d = Task(item=data, cre_date=datetime.now(), deadline=datetime.now(), priority='0')
            d.save()
        # 削除
        if request.POST.getlist('check'):
            for data in request.POST.getlist('check'):
                Task.objects.filter(id=data).delete()

    return render(request, 'todo/index.html', {'task_list': Task.objects.all()})


def archive(request):
    return HttpResponse("You're looking archive page.")


def detail(request, pk):
    # task_detail = get_object_or_404(Task, pk=pk)
    # dict_item = {'item': u'ttt', 'cre_date': u'2017', 'deadline': u'2018', 'priority': 1}
    return render(request, 'todo/detail.html', {'task_list': Task.objects.filter(pk=pk)})


def form_test(request):
    if request.method == "POST":
        form = MyForm(data=request.POST)
        if form.is_valid():
            pass
    else:
        form = MyForm()
    return render(request, 'todo/form.html', {'form': form})
