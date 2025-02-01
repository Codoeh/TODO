from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from catalog.forms import TaskForm
from catalog.models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = "catalog/task_list.html"


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("catalog:task-list")


class TagListView(ListView):
    model = Tag
    template_name = "catalog/tag_list.html"