import pytest
from django.urls import reverse
from rest_framework import status

@pytest.mark.django_db
class TestSerieAPI:
    def test_listar_series(self, client, serie):
        url = reverse('serie-list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    def test_criar_serie(self, client, user):
        client.force_login(user)
        url = reverse('serie-list')
        data = {
            'titulo': 'Nova Série',
            'descricao': 'Descrição da série',
            'ano': 2024,
        }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['titulo'] == data['titulo']

    def test_atualizar_serie(self, client, serie, user):
        client.force_login(user)
        url = reverse('serie-detail', args=[serie.id])
        data = {
            'titulo': 'Título Atualizado'
        }
        response = client.patch(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['titulo'] == data['titulo']

    def test_deletar_serie(self, client, serie, user):
        client.force_login(user)
        url = reverse('serie-detail', args=[serie.id])
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT