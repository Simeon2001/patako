from rest_framework import serializers
from .models import Profile

class profile_serializer (serializers.ModelSerializer):
    

    class Meta:
        model = Profile
        fields = ['user','avatar','interest']