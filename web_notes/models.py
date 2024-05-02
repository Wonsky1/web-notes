from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Note(models.Model):
    name = models.CharField(max_length=63)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="notes")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("created_at", )
