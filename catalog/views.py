from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from catalog.forms import TaskForm, TagForm
from catalog.models import Task, Tag


@method_decorator(login_required, name="dispatch")
class TaskListView(ListView):
    model = Task
    template_name = "catalog/task_list.html"
    context_object_name = "task_list"

    def get_queryset(self):
        return (Task.objects.all().
                order_by("is_done", "-created").
                prefetch_related("tags"))


@method_decorator(login_required, name="dispatch")
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("catalog:task-list")


@method_decorator(login_required, name="dispatch")
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("catalog:task-list")


@method_decorator(login_required, name="dispatch")
class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("catalog:task-list")


@login_required
def TaskCompleteUndo(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("catalog:task-list")


@method_decorator(login_required, name="dispatch")
class TagListView(ListView):
    model = Tag
    template_name = "catalog/tag_list.html"


@method_decorator(login_required, name="dispatch")
class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("catalog:tag-list")


@method_decorator(login_required, name="dispatch")
class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("catalog:tag-list")


@method_decorator(login_required, name="dispatch")
class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("catalog:tag-list")
