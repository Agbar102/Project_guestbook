import re
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class RegisterUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password1 = serializers.CharField(min_length=8, write_only=True)
    password2 = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def validate(self, attrs):
        email = attrs.get("email")
        user = User.objects.filter(email=email)
        if user.exists():
            raise serializers.ValidationError("Этот емейл уже занят!!!")
        password1 = attrs.pop("password1")
        password2 = attrs.pop("password2")
        if password1 == password2:
            attrs["password"] = password1
        else:
            raise serializers.ValidationError("Пароли не совпадают!!!")
        if not password1[0].isupper():
            raise serializers.ValidationError("Пароль должен быть с саглавной буквы")
        if not re.search(r"\d", password1):
            raise serializers.ValidationError("Пароль должен содержать цивры")
        return attrs


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, write_only=True)

