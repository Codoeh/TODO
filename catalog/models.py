from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

class Task(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(auto_now=False, null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name="tasks")
    is_done = models.BooleanField(default=False)


    def __str__(self):
        return f"{'[✓] ' if self.is_done else '[ ] '} {self.content[:50]}"

    class Meta:
        ordering = ["is_done", "-created",]
        verbose_name = "Task"
        verbose_name_plural = "Tasks"