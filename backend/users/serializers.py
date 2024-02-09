from rest_framework import serializers

from backend.users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = CustomUser
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "role",
        )


# class UserCreationSerializer(serializers.Serializer):
#
#     username = serializers.SlugField(
#         required=True,
#         max_length=USERNAME_MAX_LENGTH,
#     )
#     email = serializers.EmailField(required=True, max_length=EMAIL_MAX_LENGTH)
#
#     def validate(self, serializer_data: dict) -> dict:
#         if (  # noqa: WPS337
#             User.objects.filter(username=serializer_data["username"]).exists()
#             ^ User.objects.filter(email=serializer_data["email"]).exists()
#         ):
#             raise serializers.ValidationError(
#                 "Пользователь с таким username или email уже существует."
#                 "Однако username и email не соответствуют друг другу.",
#             )
#
#         if serializer_data["username"] == "me":
#             raise serializers.ValidationError(
#                 "Невозможно создать пользователя с username `me`.",
#             )
#         return serializer_data
