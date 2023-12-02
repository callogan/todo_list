from django.urls import reverse_lazy
from django.views import generic

from task.models import Task


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "task/task_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    template_name = "task/task_list.html"
    success_url = reverse_lazy("task:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task


class TaskDeleteView(generic.DeleteView):
    model = Task
