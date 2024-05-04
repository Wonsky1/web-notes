from django.urls import path

from web_notes.views import (
    NoteListView,
    NoteCreateView,
    TagListView,
    TagCreateView,
    NoteUpdateView,
    NoteDeleteView,
    TagUpdateView,
    TagDeleteView,
    change_pin_status,
    change_favourite_status,
    change_archive_status,
    ArchivedNoteListView,
)


urlpatterns = [
    path("", NoteListView.as_view(), name="note-list"),
    path("archived/", ArchivedNoteListView.as_view(), name="note-archived-list"),
    path("create/", NoteCreateView.as_view(), name="note-create"),
    path("<int:pk>/update/", NoteUpdateView.as_view(), name="note-update"),
    path("<int:pk>/delete/", NoteDeleteView.as_view(), name="note-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path(
        "change-pin-status/<int:pk>/", change_pin_status, name="note-change-pin-status"
    ),
    path(
        "change-favourite-status/<int:pk>/",
        change_favourite_status,
        name="note-change-favourite-status",
    ),
    path(
        "change-archive-status/<int:pk>/",
        change_archive_status,
        name="note-change-archive-status",
    ),
]

app_name = "notes"
