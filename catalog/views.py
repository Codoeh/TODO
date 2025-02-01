from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from catalog.forms import TaskForm, TagForm
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


def TaskCompleteUndo(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("catalog:task-list")


class TagListView(ListView):
    model = Tag
    template_name = "catalog/tag_list.html"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("catalog:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("catalog:tag-list")