import pytest
from django.contrib import admin
from django.test import Client
from django.urls import reverse

from core.models import Post


@pytest.mark.django_db
def test_home_view_renderiza_template():
    Post.objects.create(
        title="Meu primeiro post",
        content="Conteúdo de teste do portfólio.",
    )

    client = Client()
    response = client.get(reverse("home"))

    assert response.status_code == 200
    assert "Meu primeiro post" in response.content.decode("utf-8")


@pytest.mark.django_db
def test_home_nao_exibe_post_nao_publicado():
    Post.objects.create(
        title="Rascunho oculto",
        content="Este conteúdo não deve aparecer.",
        published=False,
    )

    client = Client()
    response = client.get(reverse("home"))

    assert response.status_code == 200
    assert "Rascunho oculto" not in response.content.decode("utf-8")


@pytest.mark.django_db
def test_post_detail():
    post = Post.objects.create(
        title="Detalhe do post",
        content="Texto completo para a página de detalhe.",
    )

    client = Client()
    response = client.get(reverse("post_detail", args=[post.pk]))

    assert response.status_code == 200
    assert "Detalhe do post" in response.content.decode("utf-8")


@pytest.mark.django_db
def test_post_detail_nao_exibe_post_nao_publicado():
    post = Post.objects.create(
        title="Detalhe privado",
        content="Não publicado.",
        published=False,
    )

    client = Client()
    response = client.get(reverse("post_detail", args=[post.pk]))

    assert response.status_code == 404


def test_post_registrado_no_admin_com_slug_automatico():
    assert Post in admin.site._registry
    post_admin = admin.site._registry[Post]
    assert post_admin.prepopulated_fields == {"slug": ("title",)}
