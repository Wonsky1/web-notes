from web_notes.models import Tag

from django.test import TestCase
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from unittest.mock import MagicMock, patch
from web_notes.models import Note
from web_notes.views import (
    change_favourite_status,
    change_archive_status,
    change_pin_status,
)


class ChangePinStatusViewTestCase(TestCase):
    @patch("web_notes.views.Note.objects.get")
    def test_change_pin_status(self, mock_get):
        mock_note = MagicMock()
        mock_note.is_pinned = False
        mock_note.save = MagicMock()
        mock_get.return_value = mock_note

        request = HttpRequest()
        request.GET.get = MagicMock(return_value=None)
        response = change_pin_status(request, pk=1)

        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertEqual(response.url, reverse("notes:note-list"))
        self.assertTrue(mock_note.is_pinned)
        mock_note.save.assert_called_once()


class ChangeArchiveStatusViewTestCase(TestCase):
    @patch("web_notes.views.Note.objects.get")
    def test_change_archive_status(self, mock_get):
        mock_note = MagicMock()
        mock_note.is_archived = False
        mock_note.save = MagicMock()
        mock_get.return_value = mock_note

        request = HttpRequest()
        request.GET.get = MagicMock(return_value=None)
        response = change_archive_status(request, pk=1)

        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertEqual(response.url, reverse("notes:note-list"))
        self.assertTrue(mock_note.is_archived)
        mock_note.save.assert_called_once()


class ChangeFavouriteStatusViewTestCase(TestCase):
    @patch("web_notes.views.Note.objects.get")
    def test_change_favourite_status(self, mock_get):
        mock_note = MagicMock()
        mock_note.is_favourite = False
        mock_note.save = MagicMock()
        mock_get.return_value = mock_note

        request = HttpRequest()
        request.GET.get = MagicMock(return_value=None)
        response = change_favourite_status(request, pk=1)

        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertEqual(response.url, reverse("notes:note-list"))
        self.assertTrue(mock_note.is_favourite)
        mock_note.save.assert_called_once()


class NoteListViewTestCase(TestCase):

    def test_get_note_list(self):
        response = self.client.get(reverse("notes:note-list"))
        self.assertEqual(response.status_code, 200)


class ArchivedNoteListViewTestCase(TestCase):
    def test_get_archived_note_list(self):
        response = self.client.get(reverse("notes:note-archived-list"))
        self.assertEqual(response.status_code, 200)


class NoteCreateViewTestCase(TestCase):
    def test_get_create_note_form(self):
        response = self.client.get(reverse("notes:note-create"))
        self.assertEqual(response.status_code, 200)


class NoteUpdateViewTestCase(TestCase):
    def test_get_update_note_form(self):
        note = Note.objects.create(name="Test Note", description="Descr")
        response = self.client.get(reverse("notes:note-update", kwargs={"pk": note.pk}))
        self.assertEqual(response.status_code, 200)


class NoteDeleteViewTestCase(TestCase):
    def test_delete_note(self):
        note = Note.objects.create(name="Test Note", description="Descr")
        response = self.client.post(
            reverse("notes:note-delete", kwargs={"pk": note.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Note.objects.filter(pk=note.pk).exists())


class TagCreateViewTestCase(TestCase):
    def test_get_create_tag_form(self):
        response = self.client.get(reverse("notes:tag-create"))
        self.assertEqual(response.status_code, 200)


class TagListViewTestCase(TestCase):
    def test_get_tag_list(self):
        response = self.client.get(reverse("notes:tag-list"))
        self.assertEqual(response.status_code, 200)


class TagUpdateViewTestCase(TestCase):
    def test_get_update_tag_form(self):
        tag = Tag.objects.create(name="Test Tag")
        response = self.client.get(reverse("notes:tag-update", kwargs={"pk": tag.pk}))
        self.assertEqual(response.status_code, 200)


class TagDeleteViewTestCase(TestCase):
    def test_delete_tag(self):
        tag = Tag.objects.create(name="Test Tag")
        response = self.client.post(reverse("notes:tag-delete", kwargs={"pk": tag.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Tag.objects.filter(pk=tag.pk).exists())
