"""Plain Django JsonResponse views — no DRF, no database."""
import time

from django.http import JsonResponse

# Captured once at import time so /health can report process uptime.
_START_TIME = time.monotonic()

NAME = "docker-django-api"
VERSION = "1.0.0"


def index(request):
    """Service metadata."""
    return JsonResponse(
        {
            "name": NAME,
            "version": VERSION,
            "endpoints": ["/", "/health", "/api/hello"],
        }
    )


def health(request):
    """Liveness probe with process uptime in seconds."""
    return JsonResponse(
        {
            "status": "ok",
            "uptime": time.monotonic() - _START_TIME,
        }
    )


def hello(request):
    """Greet ``name`` (defaults to ``world``)."""
    name = request.GET.get("name", "world")
    return JsonResponse({"message": f"Hello, {name}!"})
