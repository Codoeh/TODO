from django.shortcuts import render
from django.views.generic import ListView
from catalog.models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = "catalog/task_list.html"