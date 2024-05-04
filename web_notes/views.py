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


class NoteListView(generic.ListView):
    model = Note

    def get_queryset(self):
        queryset = super().get_queryset()

        sorting_param = self.request.GET.get('sorting')

        if sorting_param == 'date_created_asc':
            queryset = queryset.order_by('created_at')
        elif sorting_param == "date_created_desc":
            queryset = queryset.order_by('-created_at')
        elif sorting_param == 'name_asc':
            queryset = queryset.order_by('name')
        elif sorting_param == "name_desc":
            queryset = queryset.order_by('-name')
        elif sorting_param == 'word_count_asc':
            queryset = queryset.order_by("word_count")
        elif sorting_param == 'word_count_desc':
            queryset = queryset.order_by("-word_count")
        elif sorting_param == 'unique_word_count_asc':
            queryset = queryset.order_by("unique_word_count")
        elif sorting_param == 'unique_word_count_desc':
            queryset = queryset.order_by("-unique_word_count")

        tag_filter = self.request.GET.getlist('tag_filter')
        if tag_filter:
            for tag_id in tag_filter:
                queryset = queryset.filter(tags__id=tag_id)

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        context['sorting_options'] = [
            ('', 'Default'),
            ('name_asc', 'Name: A -> Z'),
            ('name_desc', 'Name: Z -> A'),
            ('date_created_asc', 'Date Created: Oldest -> Newest'),
            ('date_created_desc', 'Date Created: Newest -> Oldest'),
            ('word_count_asc', 'Word Count: Ascending'),
            ('word_count_desc', 'Word Count: Descending'),
            ('unique_word_count_asc', 'Unique Word Count: Ascending'),
            ('unique_word_count_desc', 'Unique Word Count: Descending'),
        ]
        context['tag_list'] = Tag.objects.all()

        return context


class ArchivedNoteListView(NoteListView):
    queryset = Note.objects.prefetch_related("tags").filter(is_archived=True)


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

    def get_queryset(self):
        queryset = super().get_queryset()

        sorting_param = self.request.GET.get('sorting')
        if sorting_param == 'name_asc':
            queryset = queryset.order_by('name')
        elif sorting_param == "name_desc":
            queryset = queryset.order_by('-name')

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        context['sorting_options'] = [
            ('', 'Default'),
            ('name_asc', 'Name: A -> Z'),
            ('name_desc', 'Name: Z -> A'),
        ]

        return context


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("notes:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("notes:tag-list")
