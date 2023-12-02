from django.urls import path

from task.views import TaskListView, TaskCreateView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path(
        "create-task/", TaskCreateView.as_view(), name='create-task'
    ),
]


app_name = "todo_list"
