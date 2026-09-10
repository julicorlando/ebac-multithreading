import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_home_view():
    client = Client()
    response = client.get(reverse("home"))

    assert response.status_code == 200
    assert response.content.decode("utf-8") == "Hello World"
