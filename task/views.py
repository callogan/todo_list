from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from task.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "task/task_list.html"
    queryset = Task.objects.prefetch_related("tags")
    # print(queryset)


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    template_name = "task/task_form.html"
    success_url = reverse_lazy("task:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    template_name = "task/task_form.html"
    success_url = reverse_lazy("task:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "task/task_confirm_delete.html"
    success_url = reverse_lazy("task:task-list")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "task/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "task/tag_form.html"
    success_url = reverse_lazy("task:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "task/tag_form.html"
    success_url = reverse_lazy("task:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "task/tag_confirm_delete.html"
    success_url = reverse_lazy("task:tag-list")


def toggle_task_completion(request, pk: int):
    task = Task.objects.get(id=pk)
    task.completed = not task.completed
    task.save()
    return redirect("task:task-list")
