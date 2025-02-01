from django.contrib import admin
from catalog.models import Tag, Task


admin.site.register(Tag)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
   list_display = ("content", "datetime", "deadline", "is_done")
