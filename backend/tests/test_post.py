from http import HTTPStatus

import pytest
from posts.models import BlogPost


@pytest.mark.django_db(transaction=True)
class TestPostAPI:

    VALID_DATA = {"text": "Поменяли текст статьи"}
    post_list_url = "/api/v1/posts/"
    post_detail_url = "/api/v1/posts/{post_id}/"

    def check_post_data(self, response_data, request_method_and_url, db_post=None):
        expected_fields = ("id", "text", "user", "created_at")
        for field in expected_fields:
            assert field in response_data, (
                "Проверьте, что для авторизованного пользователя ответ на "
                f"{request_method_and_url} содержит поле `{field}` постов."
            )
        if db_post:
            assert response_data["user"] == db_post.user.username, (
                "Проверьте, что для авторизованного пользователя ответ на "
                f"{request_method_and_url} содержит поле `user` с "
                "именем автора каждого из постов."
            )
            assert response_data["id"] == db_post.id, (
                "Проверьте, что для авторизованного пользователя ответ на "
                f"{request_method_and_url} содержится корректный `id` поста."
            )

    def test_post_not_found(self, client, post):
        response = client.get(self.post_list_url)

        assert response.status_code != HTTPStatus.NOT_FOUND, (
            f"Эндпоинт `{self.post_list_url}` не найден, проверьте настройки " "в *urls.py*."
        )

    def test_post_list_not_auth(self, client, post):
        response = client.get(self.post_list_url)

        assert response.status_code == HTTPStatus.UNAUTHORIZED, (
            "Проверьте, что GET-запрос неавторизованного пользователя к "
            f"`{self.post_list_url}` возвращает ответ со статусом 401."
        )

    def test_post_single_not_auth(self, client, post):
        response = client.get(self.post_detail_url.format(post_id=post.id))

        assert response.status_code == HTTPStatus.OK, (
            "Проверьте, что GET-запрос неавторизованного пользователя к "
            f"`{self.post_detail_url}` возвращает ответ со статусом 200."
        )

    def test_post_create_auth_with_invalid_data(self, user_client):
        posts_count = BlogPost.objects.count()
        response = user_client.post(self.post_list_url, data={})
        assert response.status_code == HTTPStatus.BAD_REQUEST, (
            "Проверьте, что для авторизованного пользователя POST-запрос с "
            f"некорректными данными к `{self.post_list_url}` возвращает ответ "
            "со статусом 400."
        )
        assert posts_count == BlogPost.objects.count(), (
            f"Проверьте, что POST-запрос с некорректными данными, "
            f"отправленный к `{self.post_list_url}`, не создаёт новый пост."
        )

    def test_post_unauth_create(self, client, user, another_user):
        posts_conut = BlogPost.objects.count()

        data = {"user": another_user.id, "text": "Статья номер 3"}
        assert_msg = (
            "Проверьте, что POST-запрос неавторизованного пользователя к "
            f"`{self.post_list_url}` возвращает ответ со статусом 401."
        )
        try:
            response = client.post(self.post_list_url, data=data)
        except ValueError as error:
            raise AssertionError(assert_msg + ("\nВ процессе выполнения запроса произошла ошибка: " f"{error}"))
        assert response.status_code == HTTPStatus.UNAUTHORIZED, assert_msg

        assert posts_conut == BlogPost.objects.count(), (
            "Проверьте, что POST-запрос неавторизованного пользователя к "
            f"`{self.post_list_url}` не создаёт новый пост."
        )

    @pytest.mark.parametrize("http_method", ("put", "patch"))
    def test_post_change_not_auth_with_valid_data(self, client, post, http_method):
        request_func = getattr(client, http_method)
        response = request_func(self.post_detail_url.format(post_id=post.id), data=self.VALID_DATA)
        http_method = http_method.upper()
        assert response.status_code == HTTPStatus.UNAUTHORIZED, (
            f"Проверьте, что {http_method}-запрос неавторизованного "
            f"пользователя к `{self.post_detail_url}` возвращает ответ со "
            "статусом 401."
        )
        db_post = BlogPost.objects.filter(id=post.id).first()
        assert db_post.text != self.VALID_DATA["text"], (
            f"Проверьте, что {http_method}-запрос неавторизованного "
            f"пользователя к `{self.post_detail_url}` не вносит изменения в "
            "пост."
        )

    def test_post_delete_by_author(self, user_client, post):
        response = user_client.delete(self.post_detail_url.format(post_id=post.id))
        assert response.status_code == HTTPStatus.NO_CONTENT, (
            "Проверьте, что для автора поста DELETE-запрос к "
            f"`{self.post_detail_url}` возвращает ответ со статусом 204."
        )

        test_post = BlogPost.objects.filter(id=post.id).first()
        assert not test_post, "Проверьте, что DELETE-запрос автора поста к " " `/api/v1/posts/{id}/` удаляет этот пост."

    def test_post_unauth_delete_current(self, client, post):
        response = client.delete(self.post_detail_url.format(post_id=post.id))
        assert response.status_code == HTTPStatus.UNAUTHORIZED, (
            "Проверьте, что DELETE-запрос неавторизованного пользователя "
            f"к `{self.post_detail_url}` вернёт ответ со статусом 401."
        )
        test_post = BlogPost.objects.filter(id=post.id).first()
        assert test_post, (
            "Проверьте, что DELETE-запрос неавторизованного пользователя "
            f"к `{self.post_detail_url}` не удаляет запрошенный пост."
        )

    def test_post_delete_not_author(self, user_client, another_post):
        response = user_client.delete(self.post_detail_url.format(post_id=another_post.id))
        assert response.status_code == HTTPStatus.FORBIDDEN, (
            "Проверьте, что DELETE-запрос авторизованного пользователя, "
            f"отправленный на `{self.post_detail_url}` к чужому посту, вернёт "
            "ответ со статусом 403."
        )

        test_post = BlogPost.objects.filter(id=another_post.id).first()
        assert test_post, "Проверьте, что авторизованный пользователь не может удалить " "чужой пост."
