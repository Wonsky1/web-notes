from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("web_notes.urls", namespace="web_notes")),
    path("django_select2/", include("django_select2.urls")),
]
