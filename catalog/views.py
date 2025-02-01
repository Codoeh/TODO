from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from catalog.forms import TaskForm
from catalog.models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = "catalog/task_list.html"


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("catalog:task-list")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("catalog:task-list")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("catalog:task-list")


class TagListView(ListView):
    model = Tag
    template_name = "catalog/tag_list.html"