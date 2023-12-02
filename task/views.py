from django.shortcuts import render
from django.views import generic

from task.models import Task


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task


class TaskUpdateView(generic.UpdateView):
    model = Task


class TaskDeleteView(generic.DeleteView):
    model = Task
