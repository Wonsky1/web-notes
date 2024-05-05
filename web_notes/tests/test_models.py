from django.test import TestCase
from web_notes.models import Tag, Note


class TagModelTestCase(TestCase):
    def test_tag_creation(self):
        tag = Tag.objects.create(name="Test Tag", color="#00FF00")
        self.assertEqual(tag.name, "Test Tag")
        self.assertEqual(tag.color, "#00FF00")


class NoteModelTestCase(TestCase):
    def test_note_creation(self):
        note = Note.objects.create(name="Test Note", description="one two one")
        self.assertEqual(note.name, "Test Note")
        self.assertEqual(note.is_archived, False)
        self.assertEqual(note.is_favourite, False)
        self.assertEqual(note.is_pinned, False)
        self.assertEqual(note.word_count, 3)
        self.assertEqual(note.unique_word_count, 2)
