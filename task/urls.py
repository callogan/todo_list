from django.urls import path

from task.views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, toggle_task_completion

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path(
        "task/create-task/",
        TaskCreateView.as_view(),
        name='create-task'
    ),
    path(
        "task/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name='update-task'
    ),
    path(
        "task/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="delete-task",
    ),
    path(
        "task/<int:pk>/toggle_completion/",
        toggle_task_completion,
        name="toggle-task-completion"
    ),
]


app_name = "todo_list"
