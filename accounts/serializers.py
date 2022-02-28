from .models import User,is_mobile,is_email,Profile
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

# def is_valid_username(value):
#     if not is_email(value) and not is_mobile(value):
#         return serializers.ValidationError("Enter Email or Phone")
#
# class UserVerifySerializers(serializers.Serializer):
#     username = serializers.CharField(validators=[is_valid_username])
#     verify_code = serializers.IntegerField()


# class ProfileSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Profile

