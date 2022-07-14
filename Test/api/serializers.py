from rest_framework import serializers
from Profile.models import Profile


class Profileserializer (serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'