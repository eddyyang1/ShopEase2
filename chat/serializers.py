from rest_framework import serializers
from .models import Conversation, Message
from django.contrib.auth.models import User

# Serializer for the Message model
class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField()  # You can change this to display sender's username or full name if you prefer

    class Meta:
        model = Message
        fields = ('id', 'sender', 'content', 'timestamp')

# Serializer for the Conversation model
class ConversationSerializer(serializers.ModelSerializer):
    participants = serializers.StringRelatedField(many=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ('id', 'participants', 'messages', 'created_at')
