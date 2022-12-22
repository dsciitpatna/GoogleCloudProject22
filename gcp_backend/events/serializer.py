from rest_framework import serializers
from .models import Event, Subscription, Tag
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields= "__all__"

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields="__all__"

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields="__all__"
