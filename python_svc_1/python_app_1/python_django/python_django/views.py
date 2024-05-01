from django.http import JsonResponse

from django.core.handlers.wsgi import WSGIRequest


def healthcheck(request: WSGIRequest):
    """
    Simple view to check if the API is working.
    """
    return JsonResponse({'message': 'Django REST Framework is up and running!'})