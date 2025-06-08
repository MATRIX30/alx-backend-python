from django.shortcuts import render
from rest_framework import viewsets, status, filters
from .models import User, Conversation, Message
from .serializers import UserSerializer, ConversationSerializer, MessageSerializer
from .permissions import  IsOwnerOrParticipant, IsParticipantOfConversation



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes =[IsOwnerOrParticipant, IsParticipantOfConversation]

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes =[IsOwnerOrParticipant, IsParticipantOfConversation]

# Create your views here.
