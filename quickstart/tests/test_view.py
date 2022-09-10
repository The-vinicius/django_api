import pytest
from django_fakeredis import FakeRedis
from django.urls import reverse

@pytest.mark.django_db
@FakeRedis("core.settings")
def test_view_cache(client, aluno_criado):
    url = reverse('cache')
    response = client.get(url)
    assert b'vini' in response.content

