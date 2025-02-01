from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(auto_now=False, null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    is_done = models.BooleanField(default=False)


    def __str__(self):
        return self.content

    class Meta:
        ordering = ["is_done", ]