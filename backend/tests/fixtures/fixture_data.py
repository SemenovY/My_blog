import pytest
from posts.models import BlogPost


@pytest.fixture
def post(user):
    return BlogPost.objects.create(text="Тестовый пост 1", user=user)


@pytest.fixture
def post_2(user):
    return BlogPost.objects.create(text="Тестовый пост 12342341", user=user)


@pytest.fixture
def another_post(another_user):
    return BlogPost.objects.create(text="Тестовый пост 2", user=another_user)
