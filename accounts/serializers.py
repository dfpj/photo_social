from .models import User,is_mobile,is_email
from rest_framework import serializers


class UserCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password','verify_code','is_active']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_active': {'read_only': True},
            'verify_code': {'read_only': True},
        }

def is_valid_username(value):
    if not is_email(value) and not is_mobile(value):
        return serializers.ValidationError("Enter Email or Phone")

class UserVerifySerializers(serializers.Serializer):
    username = serializers.CharField(validators=[is_valid_username])
    verify_code = serializers.IntegerField()


