from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from django.contrib.auth.models import User

# Viewset for the Conversation model
class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]  # Ensure only authenticated users can access this

    # Action to create a new conversation
    @action(detail=False, methods=['post'])
    def create_conversation(self, request):
        participants = request.data.get('participants', [])
        if not participants:
            return Response({'detail': 'Participants are required'}, status=400)

        # Check if all participants exist
        users = User.objects.filter(id__in=participants)
        if users.count() != len(participants):
            return Response({'detail': 'Some users do not exist'}, status=400)

        # Create the conversation
        conversation = Conversation.objects.create()
        conversation.participants.set(users)
        conversation.save()

        return Response(ConversationSerializer(conversation).data, status=201)

    # Action to get messages for a specific conversation
    @action(detail=True, methods=['get'])
    def get_messages(self, request, pk=None):
        conversation = self.get_object()
        messages = Message.objects.filter(conversation=conversation)
        return Response(MessageSerializer(messages, many=True).data)

# Viewset for the Message model
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]  # Ensure only authenticated users can access this

    # Action to send a message to a conversation
    @action(detail=True, methods=['post'])
    def send_message(self, request, pk=None):
        conversation = self.get_object()
        content = request.data.get('content', '')

        if not content:
            return Response({'detail': 'Message content is required'}, status=400)

        message = Message.objects.create(
            conversation=conversation,
            sender=request.user,
            content=content
        )

        return Response(MessageSerializer(message).data, status=201)
