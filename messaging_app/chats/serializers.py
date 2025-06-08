from rest_framework import serializers
from .models import Conversation, User, Message

class UserSerializer(serializers.ModelSerializer):
    
    
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'role']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    class Meta:
        model = User
        fields = '__all__'
        
        
class MessageSerializer(serializers.ModelSerializer):
    # sender = serializers.StringRelatedField(read_only = True)
    sender = serializers.CharField(source='sender.username', read_only=True)
    class Meta:
        model = Message
        fields = ['message_id', 'conversation', 'sender', 'message_body']

class ConversationSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.all()
    )

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'messages', 'created_at', 'updated_at']
    
    def validate(self, data):
        """
        add custom validation logic to your serializer. Specifically, it checks that any conversation being created or updated has at least two participants. If there are fewer 
        than two, it raises a ValidationError with a helpful message. 
        """
        if 'participants' in data and len(data['participants']) < 2:
            raise serializers.ValidationError("A conversation must have at least two participants.")
        return data