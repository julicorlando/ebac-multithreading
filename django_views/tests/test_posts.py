import pytest
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.test import Client

from core.models import Post


@pytest.mark.django_db
def test_post_slug_is_created_from_title():
    post = Post.objects.create(
        title="Meu Primeiro Post",
        content="Conteúdo de teste",
    )

    assert post.slug == "meu-primeiro-post"


@pytest.mark.django_db
def test_duplicate_titles_receive_unique_slugs():
    first = Post.objects.create(title="Post Repetido", content="Primeiro")
    second = Post.objects.create(title="Post Repetido", content="Segundo")

    assert first.slug == "post-repetido"
    assert second.slug == "post-repetido-2"


def test_post_is_registered_in_django_admin():
    assert Post in admin.site._registry
    post_admin = admin.site._registry[Post]
    assert post_admin.prepopulated_fields == {"slug": ("title",)}


@pytest.mark.django_db
def test_superuser_can_see_posts_in_admin():
    user_model = get_user_model()
    user_model.objects.create_superuser(
        username="superuser",
        email="superuser@example.com",
        password="senha-forte-123",
    )

    client = Client()
    assert client.login(username="superuser", password="senha-forte-123")

    response = client.get("/admin/")

    assert response.status_code == 200
    assert "Posts" in response.content.decode("utf-8")
