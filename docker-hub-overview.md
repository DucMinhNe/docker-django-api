# minhle202/django-api

A production-grade, lightweight **Python 3.12 + Django 5 + Gunicorn** REST API
starter. Serves JSON via plain Django `JsonResponse` views — **no DRF, no
database** — so the image is tiny and boots instantly. Part of the `minhle202`
family of Docker Hub starter images by **Lê Đức Minh**.

## Tags

- `latest` — multi-arch (**linux/amd64** + **linux/arm64**).

## Quick start

```bash
docker pull minhle202/django-api
docker run --rm -p 8000:8000 minhle202/django-api

curl http://localhost:8000/
curl http://localhost:8000/health
curl "http://localhost:8000/api/hello?name=Minh"
```

## Endpoints

- `GET /` → `{"name","version","endpoints"}`
- `GET /health` → `{"status":"ok","uptime":<seconds>}`
- `GET /api/hello?name=` → `{"message":"Hello, <name>!"}` (`name` defaults to `world`)

## Environment variables

- `SECRET_KEY` — Django secret key. A dev-only fallback ships in the image;
  **always set this in production.**
- `PORT` — port Gunicorn binds to (default `8000`).

## Features

- Python 3.12-slim base.
- Django 5 + Gunicorn (2 workers × 4 threads).
- Multi-stage build with an isolated `venv`.
- Non-root user (uid 10001).
- Built-in `HEALTHCHECK` on `/health`.
- `DEBUG=False` and env-driven `SECRET_KEY` by default.

## Source

https://github.com/DucMinhNe/docker-django-api
