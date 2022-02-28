from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password','verify_code','is_active']
        extra_kwargs = {
            'password': {'write_only': True,'required':False},
            'verify_code': {'required':False},
            'is_active': {'required':False},
            'username': {'required':False},
        }
