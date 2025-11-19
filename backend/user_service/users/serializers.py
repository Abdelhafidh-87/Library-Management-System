from rest_framework import serializers
from .models import User, UserProfile


# ---------------------------------------------------------
# User Serializers
# ---------------------------------------------------------

class UserSerializer(serializers.ModelSerializer):
    """Serializer pour renvoyer les infos utilisateur sans le mot de passe"""
    
    class Meta:
        model = User
        fields = [
            "id", "email", "username", "first_name",
            "last_name", "phone", "role", "is_active",
            "max_loans", "created_at", "updated_at"
        ]
