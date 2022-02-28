from rest_framework import serializers
from .models import Profile

class ProfileSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    gender = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields='__all__'
        extra_kwargs = {
            'user': {'read_only': True, 'required': False},
        }

    def get_gender(self, obj):
        return obj.get_gender_display()