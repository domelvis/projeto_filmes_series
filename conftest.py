import pytest
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
import factory
from factory.django import DjangoModelFactory
from series.models import Serie
from reviews.models import Review

User = get_user_model()

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')
    password = factory.PostGenerationMethodCall('set_password', 'password123')
    is_active = True

class SerieFactory(DjangoModelFactory):
    class Meta:
        model = Serie

    titulo = factory.Sequence(lambda n: f'Série {n}')
    descricao = factory.Faker('text')
    ano = factory.Faker('year')
    criado_por = factory.SubFactory(UserFactory)
    imagem = factory.LazyAttribute(
        lambda _: SimpleUploadedFile('test.jpg', b'file_content', content_type='image/jpeg')
    )

class ReviewFactory(DjangoModelFactory):
    class Meta:
        model = Review

    serie = factory.SubFactory(SerieFactory)
    usuario = factory.SubFactory(UserFactory)
    texto = factory.Faker('text')
    avaliacao = factory.Faker('random_int', min=1, max=5)

@pytest.fixture
def user():
    return UserFactory()

@pytest.fixture
def admin_user():
    return UserFactory(is_staff=True, is_superuser=True)

@pytest.fixture
def serie():
    return SerieFactory()

@pytest.fixture
def review():
    return ReviewFactory()

@pytest.fixture
def serie_com_reviews():
    serie = SerieFactory()
    ReviewFactory.create_batch(3, serie=serie)
    return serie