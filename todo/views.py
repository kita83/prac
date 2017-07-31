from django.shortcuts import render
from todo.models import Task
from django.http import HttpResponse


def index(request):
    task_list = Task.objects.all()
    context = {'task_list': task_list}
    return render(request, 'todo/index.html', context)


def archive(request):
    return HttpResponse("You're looking archive page.")
