# Genz/middleware.py
import logging

logger = logging.getLogger(__name__)

from django.http import HttpResponsePermanentRedirect

class RedirectToWwwMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f"Request host: {request.get_host()}")
        host = request.get_host()
        if host == "gen-zit.com":
            return HttpResponsePermanentRedirect("https://www.gen-zit.com" + request.path)
        response = self.get_response(request)
        return response