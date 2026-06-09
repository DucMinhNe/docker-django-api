"""
Minimal Django 5 settings for a lightweight REST API starter.

No database, no DRF, no models — just URLconf + JsonResponse views.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY: read SECRET_KEY from the environment in production.
# The fallback is for local/dev use only — set -e SECRET_KEY=... when deploying.
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-dev-fallback-change-me-in-production",
)

DEBUG = False

# Behind a proxy / running in a container; host validation is delegated upstream.
ALLOWED_HOSTS = ["*"]

# Keep the stack light: no admin, auth, sessions, messages or DB-backed apps.
INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "api",
]

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = []

WSGI_APPLICATION = "config.wsgi.application"

# No database needed for this starter.
DATABASES = {}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = False
USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
