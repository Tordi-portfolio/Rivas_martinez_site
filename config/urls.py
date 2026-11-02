from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("django-admin/", admin.site.urls),   # built-in Django admin (staff only)
    path("", include("core.urls")),
]
