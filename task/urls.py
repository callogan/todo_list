from django.urls import path

from task.views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path(
        "task/create-task/", TaskCreateView.as_view(), name='create-task'
    ),
    path(
        "task/<int:pk>/update/", TaskUpdateView.as_view(), name='update-task'
    ),
]


app_name = "todo_list"
