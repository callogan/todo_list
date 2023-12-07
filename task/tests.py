from django.test import TestCase
from django.urls import reverse
from django.forms import CharField

from .forms import TaskCreateForm
from .models import Task, Tag


class TaskViewsTestCase(TestCase):

    def setUp(self):
        self.task = Task.objects.create(content="Test task")
        self.tag = Tag.objects.create(name="Test tag")

    def test_task_list_view(self):
        url = reverse("task:task-list")

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task/task_list.html")

        self.assertIn("task_list", response.context)
        task_list = response.context["task_list"]
        self.assertIsNotNone(task_list)

        self.assertGreater(len(task_list), 0)

        for task in task_list:
            self.assertContains(response, task.content)

    def test_task_create_view(self):
        url = reverse("task:create-task")

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)
        self.assertIsInstance(response.context["form"], TaskCreateForm)

    def test_task_update_view(self):
        url = reverse("task:update-task", kwargs={"pk": self.task.pk})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)
        self.assertIn("object", response.context)
        self.assertIsInstance(response.context["form"], TaskCreateForm)
        self.assertEqual(response.context["object"], self.task)

    def test_task_delete_view(self):
        url = reverse("task:delete-task", kwargs={"pk": self.task.pk})

        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())

        self.assertRedirects(response, reverse("task:task-list"))

    def test_toggle_task_completion_view(self):
        url = reverse("task:toggle-task-completion", kwargs={"pk": self.task.pk})

        initial_completed_status = self.task.completed

        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)

        self.task.refresh_from_db()

        self.assertNotEqual(initial_completed_status, self.task.completed)

        self.assertRedirects(response, reverse("task:task-list"), target_status_code=302, fetch_redirect_response=False)

    def test_tag_list_view(self):
        url = reverse("task:tag-list")

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task/tag_list.html")

        self.assertIn("tag_list", response.context)
        tag_list = response.context["tag_list"]
        self.assertIsNotNone(tag_list)

        self.assertGreater(len(tag_list), 0)

        for tag in tag_list:
            self.assertContains(response, tag.name)

    def test_tag_create_view(self):
        url = reverse('task:create-tag')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task/tag_form.html")

        self.assertIn("form", response.context)

        form = response.context["form"]

        self.assertIn("name", form.fields)

        self.assertIsInstance(form.fields["name"], CharField)

    def test_tag_update_view(self):
        url = reverse("task:update-tag", kwargs={"pk": self.tag.pk})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task/tag_form.html")

        self.assertIn("form", response.context)

        form = response.context["form"]

        self.assertIn("name", form.fields)

        self.assertIsInstance(form.fields["name"], CharField)

    def test_tag_delete_view(self):
        url = reverse("task:delete-tag", kwargs={"pk": self.tag.pk})

        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Tag.objects.filter(pk=self.tag.pk).exists())

        self.assertRedirects(response, reverse("task:tag-list"))
