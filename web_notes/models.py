from django.core.exceptions import ValidationError
from django.db import models


def validate_color(value):
    if not value.startswith('#') or len(value) != 7:
        raise ValidationError('Invalid color format (must be #RRGGBB)')


class Tag(models.Model):
    name = models.CharField(max_length=63)
    color = models.CharField(max_length=7, default="#FF0000", validators=[validate_color])

    def __str__(self):
        return self.name

    def clean_color(self):
        color = self.cleaned_data['color']
        if not color.startswith('#') or len(color) != 7:
            raise ValidationError('Invalid color format (must be #RRGGBB)')
        return color


class WordCountField(models.IntegerField):

    def __init__(self, unique_count = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.unique_count = unique_count

    def contribute_to_class(self, cls, name, **kwargs):
        super().contribute_to_class(cls, name, **kwargs)
        models.signals.post_save.connect(self.update_word_count, sender=cls)

    def update_word_count(self, instance, **kwargs):
        if self.unique_count:
            word_count = self.calculate_unique_word_count(instance)
        else:
            word_count = self.calculate_word_count(instance)
        if getattr(instance, self.attname) != word_count:
            setattr(instance, self.attname, word_count)
            instance.save(update_fields=[self.attname])

    @staticmethod
    def calculate_word_count(instance):
        description = getattr(instance, 'description', '')
        return len(description.split())

    @staticmethod
    def calculate_unique_word_count(instance):
        description = getattr(instance, 'description', '')
        return len(set(description.split()))


class Note(models.Model):
    name = models.CharField(max_length=63)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name="notes", blank=True)
    is_pinned = models.BooleanField(default=False)
    is_favourite = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    word_count = WordCountField(default=0, editable=False)
    unique_word_count = WordCountField(default=0, editable=False, unique_count=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-is_pinned", "-is_favourite", "-created_at", )
