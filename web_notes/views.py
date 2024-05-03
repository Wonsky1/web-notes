from django.http import HttpResponseRedirect, HttpRequest
from django.urls import reverse_lazy, reverse
from django.views import generic

from web_notes.forms import TagForm, NoteForm
from web_notes.models import Note, Tag


def change_pin_status(request: HttpRequest, pk: int) -> HttpResponseRedirect:
    referring_page = request.GET.get('referring_page')
    note = Note.objects.get(id=pk)
    note.is_pinned = not note.is_pinned
    note.save()
    return HttpResponseRedirect(reverse("notes:note-list")) if not referring_page else HttpResponseRedirect(referring_page)


def change_archive_status(request: HttpRequest, pk: int) -> HttpResponseRedirect:
    referring_page = request.GET.get('referring_page')
    note = Note.objects.get(id=pk)
    note.is_archived = not note.is_archived
    note.save()
    return HttpResponseRedirect(reverse("notes:note-list")) if not referring_page else HttpResponseRedirect(referring_page)


def change_favourite_status(request: HttpRequest, pk: int) -> HttpResponseRedirect:
    referring_page = request.GET.get('referring_page')
    note = Note.objects.get(id=pk)
    note.is_favourite = not note.is_favourite
    note.save()
    return HttpResponseRedirect(reverse("notes:note-list")) if not referring_page else HttpResponseRedirect(referring_page)


class ArchivedNoteListView(generic.ListView):
    model = Note
    queryset = Note.objects.prefetch_related("tags").filter(is_archived=True)


class NoteListView(generic.ListView):
    model = Note
    queryset = Note.objects.prefetch_related("tags").filter(is_archived=False)


class NoteCreateView(generic.CreateView):
    model = Note
    form_class = NoteForm
    success_url = reverse_lazy("notes:note-list")


class NoteUpdateView(generic.UpdateView):
    model = Note
    form_class = NoteForm
    success_url = reverse_lazy("notes:note-list")


class NoteDeleteView(generic.DeleteView):
    model = Note
    success_url = reverse_lazy("notes:note-list")


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("notes:tag-list")


class TagListView(generic.ListView):
    model = Tag


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("notes:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("notes:tag-list")
