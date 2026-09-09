from django.urls import path

from .views import async_view

urlpatterns = [
    path("async/", async_view, name="async-view"),
]
