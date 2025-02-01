from django import forms

from catalog.models import Tag, Task


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    deadline = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            attrs={'type': 'date'}))

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags", "is_done",]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
