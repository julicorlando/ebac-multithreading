import pytest
from django.test import AsyncClient
from django.urls import reverse


@pytest.mark.asyncio
@pytest.mark.django_db
async def test_async_view():
    client = AsyncClient()
    response = await client.get(reverse("async-view"))

    assert response.status_code == 200

    data = response.json()
    assert data["message"] == "View assíncrona executada com sucesso"
    assert data["results"] == [100, 400, 900]
    assert data["total"] == 1400
