from django.shortcuts import render
from rest_framework import viewsets, status, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import User, Conversation, Message
from .serializers import UserSerializer, ConversationSerializer, MessageSerializer
from .permissions import  IsOwnerOrParticipant, IsParticipantOfConversation
from .pagination import MessagePagination
from .filters import MessageFilter


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes =[IsOwnerOrParticipant, IsParticipantOfConversation]
class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    pagination_class = MessagePagination
    filterset_class =  MessageFilter

    def get_queryset(self):
        # Only show messages in conversations the user participates in
        conversation_id = self.request.query_params.get('conversation_id')
        if conversation_id:
            try:
                conversation = Conversation.objects.get(pk=conversation_id)
            except Conversation.DoesNotExist:
                return Message.objects.none()
            if self.request.user not in conversation.participants.all():
                self.permission_denied(
                    self.request,
                    message="You are not a participant in this conversation.",
                    code=status.HTTP_403_FORBIDDEN
                )
            return Message.objects.filter(conversation=conversation)
        # Otherwise, show all messages the user can see
        return Message.objects.filter(conversation__participants=self.request.user)

# Create your views here.
