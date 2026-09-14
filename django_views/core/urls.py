from django.urls import path

from .views import home, post_detail

urlpatterns = [
    path("home/", home, name="home"),
    path("post/<int:pk>/", post_detail, name="post_detail"),
]
