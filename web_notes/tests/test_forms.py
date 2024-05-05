# from django.test import TestCase
# from web_notes.forms import NoteForm, TagForm
#
#
# class NoteFormTests(TestCase):
#     def test_note_form_valid(self):
#         form_data = {
#             "name": "Test Note",
#             "description": "This is a test note",
#         }
#         form = NoteForm(data=form_data)
#         self.assertTrue(form.is_valid())
#
#     def test_note_form_invalid(self):
#         form_data = {
#             "description": "This is a test note",
#         }
#         form = NoteForm(data=form_data)
#         self.assertFalse(form.is_valid())
#
#
# class TagFormTests(TestCase):
#     def test_tag_form_valid(self):
#         form_data = {
#             "name": "Test Tag",
#             "color": "#FF0000",
#         }
#         form = TagForm(data=form_data)
#         self.assertTrue(form.is_valid())
#
#     def test_tag_form_invalid(self):
#         form_data = {
#             "name": "Test Tag",
#         }
#         form = TagForm(data=form_data)
#         self.assertFalse(form.is_valid())
#
#     def test_tag_color_validation(self):
#         form_data = {
#             "name": "Test Tag",
#             "color": "invalid_color",
#         }
#         form = TagForm(data=form_data)
#         self.assertFalse(form.is_valid())
#         self.assertIn("color", form.errors)
