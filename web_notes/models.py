from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Note(models.Model):
    name = models.CharField(max_length=63)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="notes", blank=True)
    is_pinned = models.BooleanField(default=False)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-is_pinned", "-created_at", )
