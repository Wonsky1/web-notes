from django import forms
from django_select2.forms import ModelSelect2MultipleWidget

from web_notes.models import Tag, Note


class NoteForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=ModelSelect2MultipleWidget(
            model=Tag,
            search_fields=['name__icontains'],
            attrs={'data-minimum-input-length': 0}
        ),
        required=False,
    )
    class Meta:
        model = Note
        fields = ["name", "description", "tags"]


class TagForm(forms.ModelForm):
    color = forms.CharField(
        label='Color', max_length=7,
        widget=forms.TextInput(attrs={'type': 'color'})
    )

    class Meta:
        model = Tag
        fields = "__all__"
