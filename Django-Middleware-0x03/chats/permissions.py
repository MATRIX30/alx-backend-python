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


class IsParticipantOfConversation(permissions.BasePermission):
    """
    Allow only authenticated users who are participants in a conversation
    to send, view, update, and delete messages.
    """

    def has_permission(self, request, view):
        # Only allow authenticated users
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # For Conversation: user must be a participant
        if hasattr(obj, 'participants'):
            return request.user in obj.participants.all()

        # For Message: user must be sender or a participant in the conversation
        if hasattr(obj, 'sender') and hasattr(obj, 'conversation'):
            if request.method in ['PUT', 'PATCH', 'DELETE']:
                # Only sender can update or delete their message
                return obj.sender == request.user
            # Any participant can view or create
            return (
                obj.sender == request.user or
                request.user in obj.conversation.participants.all()
            )
        return False