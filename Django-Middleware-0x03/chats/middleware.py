from datetime import datetime
from django.http import HttpResponseForbidden

class RequestLoggingMiddleware:
    """
    Middleware to log each user's request with timestamp, user, and request path.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        user = request.user if hasattr(request, 'user') and request.user.is_authenticated else 'Anonymous'
        # Prepare the log entry with current timestamp, user, and request path.
        log_entry = f"{datetime.now()} - User: {user} - Path: {request.path}\n"
        
        with open('requests.log', 'a') as log_file:
            log_file.write(log_entry)
        
        response = self.get_response(request)
        return response

class RestrictAccessByTimeMiddleware:
    """
    Middleware to restrict chat access outside 6PM to 9PM.
    Returns 403 Forbidden if accessed outside allowed hours.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_hour = datetime.now().hour
        # Allow access only between 18 (6PM) and 21 (9PM), inclusive of 18, exclusive of 21
        if not (18 <= current_hour < 21):
            return HttpResponseForbidden("Access to chat is only allowed between 6PM and 9PM.")
        return self.get_response(request)
