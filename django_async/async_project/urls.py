from django.urls import include, path

urlpatterns = [
    path("", include("async_app.urls")),
]
