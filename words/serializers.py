import re
from django.contrib.auth import get_user_model

from rest_framework import serializers


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Сериалайзер пользователя"""
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'role',
        )
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=User.objects.all(), fields=['email', 'username']
            )
        ]

    def validate_username(self, value):
        pattern = re.compile('^[\\w]{3,}')
        if re.match(pattern=pattern, string=value) is None:
            raise serializers.ValidationError('Недопустимые символы.')
        return value

    def validate(self, data):
        email = data.get('email', None)
        if User.objects.filter(email=email).exists():
            if data['username'] != User.objects.get(email=email).username:
                raise serializers.ValidationError(
                    'Этот email занят.'
                )

        return super().validate(data)


class MeRoleSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        read_only_fields = ('role',)


class NewUserSerializer(serializers.ModelSerializer):
    """Сериалайзер нового пользоватея"""
    class Meta:
        model = User
        fields = (
            'username',
            'email'
        )

    def validate_username(self, value):
        pattern = re.compile('^[\\w]{3,}')
        if re.match(pattern=pattern, string=value) is None:
            raise serializers.ValidationError('Недопустимые символы.')
        return value


class TokenSerializer(serializers.ModelSerializer):
    """Сериалайзер JWT-токена."""
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')
