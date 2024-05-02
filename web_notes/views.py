from django.http import HttpResponseRedirect, HttpRequest
from django.urls import reverse_lazy, reverse
from django.views import generic

from web_notes.forms import TagForm, NoteForm
from web_notes.models import Note, Tag


class NoteListView(generic.ListView):
    model = Note
    queryset = Note.objects.prefetch_related("tags")


class NoteCreateView(generic.CreateView):
    model = Note
    form_class = NoteForm
    success_url = reverse_lazy("notes:note-list")


class NoteUpdateView(generic.UpdateView):
    model = Note
    success_url = reverse_lazy("notes:note-list")


class NoteDeleteView(generic.DeleteView):
    model = Note
    success_url = reverse_lazy("notes:note-list")


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("notes:tags-list")


class TagListView(generic.ListView):
    model = Tag


class TagUpdateView(generic.UpdateView):
    model = Tag
    success_url = reverse_lazy("notes:tags-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("notes:tags-list")
