from rest_framework import permissions

class IsOwnerOrParticipant(permissions.BasePermission):
    """
    Custom permission to only allow users to access their own messages and conversations.
    """
    def has_object_permission(self, request, view, obj):
        # For Conversation: check if user is a participant
        if hasattr(obj, 'participants'):
            return request.user in obj.participants.all()
        # For Message: check if user is the sender or a participant in the conversation
        if hasattr(obj, 'sender'):
            return obj.sender == request.user or request.user in obj.conversation.participants.all()
        return False
