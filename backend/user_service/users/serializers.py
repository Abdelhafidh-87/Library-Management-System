from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, UserProfile


# -------------------------
# User Serializers
# -------------------------

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id", "email", "username", "first_name",
            "last_name", "phone", "role", "is_active",
            "max_loans", "created_at", "updated_at"
        ]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "email", "username", "password",
            "first_name", "last_name", "phone"
        ]

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                "Le mot de passe doit contenir au moins 8 caractères."
            )
        return value

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create_user(password=password, **validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(
            email=attrs.get("email"),
            password=attrs.get("password"),
        )
        if not user:
            raise serializers.ValidationError("Email ou mot de passe incorrect.")

        attrs["user"] = user
        return attrs


# -------------------------
# UserProfile Serializers
# -------------------------

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = [
            "user",
            "bio",
            "address",
            "avatar_url",
            "birth_date",
        ]


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            "bio",
            "address",
            "avatar_url",
            "birth_date",
        ]
