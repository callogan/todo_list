from django import forms
from django.forms import DateTimeInput
from task.models import Task, Tag


class TaskCreateForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        required=False, widget=DateTimeInput(attrs={"type": "datetime-local"})
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = "__all__"
