from datetime import datetime, timedelta
from django.http import HttpResponseForbidden

class RequestLoggingMiddleware:
    """
    Middleware to log each user's request with timestamp, user, and request path.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        user = request.user if hasattr(request, 'user') and request.user.is_authenticated else 'Anonymous'
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
        if not (18 <= current_hour < 21):
            return HttpResponseForbidden("Access to chat is only allowed between 6PM and 9PM.")
        return self.get_response(request)

class OffensiveLanguageMiddleware:
    """
    Middleware to limit the number of chat messages a user can send per minute based on their IP address.
    Allows only 5 POST requests per minute per IP. Blocks further requests with 403 Forbidden.
    """
    # Dictionary to track messages per IP: {ip: [timestamps]}
    message_log = {}

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Only apply rate limiting to POST requests (i.e., sending messages)
        if request.method == 'POST':
            ip = self.get_client_ip(request)
            now = datetime.now()
            # Get or initialize the list of timestamps for this IP
            timestamps = self.message_log.get(ip, [])
            # Remove timestamps older than 1 minute
            one_minute_ago = now - timedelta(minutes=1)
            timestamps = [ts for ts in timestamps if ts > one_minute_ago]
            if len(timestamps) >= 5:
                return HttpResponseForbidden("Rate limit exceeded: Only 5 messages per minute allowed.")
            # Add current timestamp and update log
            timestamps.append(now)
            self.message_log[ip] = timestamps
        return self.get_response(request)

    def get_client_ip(self, request):
        # Get IP address from request headers or META
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip