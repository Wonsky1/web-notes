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




class Note(models.Model):
    name = models.CharField(max_length=63)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name="notes", blank=True)
    is_pinned = models.BooleanField(default=False)
    is_favourite = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-is_pinned", "-created_at", )
