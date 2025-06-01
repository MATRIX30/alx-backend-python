from rest_framework import serializers
from .models import Conversation, User, Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
        
class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Message
        fields = '__all__'

class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    participants = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Conversation
        fields = '__all__'