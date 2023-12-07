from django.urls import path

from task.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    toggle_task_completion,
    TagListView,
    TagUpdateView,
    TagCreateView,
    TagDeleteView,
)

urlpatterns = [
    path(
        "",
        TaskListView.as_view(),
        name="task-list",
    ),
    path(
        "task/create-task/",
        TaskCreateView.as_view(),
        name="create-task"
    ),
    path(
        "task/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="update-task"
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
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list"
    ),
    path(
        "tags/create_tag/",
        TagCreateView.as_view(),
        name="create-tag"
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="update-tag"
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="delete-tag"
    ),
]

app_name = "task"
