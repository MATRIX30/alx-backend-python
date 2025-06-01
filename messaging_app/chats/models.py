from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        MEMBER = 'member', 'Member'
        GUEST = 'guest', 'Guest'
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.MEMBER
    )
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=20, blank=False, null=True)
    email = models.CharField(max_length=55, blank=False, null= True)
    password = models.CharField(max_length=255, blank=False, null=False)
    
    def __str__(self):
        return f"{self.id}: {self.first_name} {self.last_name}->{self.role}"
class Conversation(models.Model):
    """
    represents a conversation involving multiple participants
    or users
    """
    #the participant uses a many-to-many relationship with the user model
    #ensuring that any conversation can have multiple users
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participants = models.ManyToManyField(User, related_name='conversations')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"converstion {self.id}: {self.participants}"
    
    
class Message(models.Model):
    """
    Represents an individual message sent in a conversation
     Each message keeps a record of the sender (linked to the User model) and 
    the conversation it belongs to (linked to the Conversation model).
    """
    message_id  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(User,on_delete=models.CASCADE, related_name='messages')
    Conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.sender.username} at {self.sent_at}"
