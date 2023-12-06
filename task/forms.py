from django import forms
from task.models import Task, Tag


class DateTimePickerInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class TaskCreateForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        required=False, widget=DateTimePickerInput
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = "__all__"
