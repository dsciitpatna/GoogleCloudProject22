from rest_framework import serializers
from user.models import User, Organization

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= "__all__"

class OrganisatinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields= "__all__"
