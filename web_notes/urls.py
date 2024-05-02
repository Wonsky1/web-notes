from django.urls import path

from web_notes.views import (
    NoteListView, NoteCreateView,
    TagListView, TagCreateView, NoteUpdateView,
    NoteDeleteView, TagUpdateView,
    TagDeleteView,
)


urlpatterns = [
    path("", NoteListView.as_view(), name="note-list"),
    path("create/", NoteCreateView.as_view(), name="note-create"),
    path("<int:pk>/update/", NoteUpdateView.as_view(), name="note-update"),
    path("<int:pk>/delete/", NoteDeleteView.as_view(), name="note-delete"),
    path("tags/", TagListView.as_view(), name="tags-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "notes"
