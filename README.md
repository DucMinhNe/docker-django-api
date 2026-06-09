# docker-django-api

A production-grade, lightweight **Python 3.12 + Django 5 + Gunicorn** REST API
starter image. It serves a few JSON endpoints using plain Django
`JsonResponse` views — **no DRF, no database, no models** — so the container
stays small and starts instantly. Part of the `minhle202` family of Docker Hub
starter images by **Lê Đức Minh**.

## Pull

```bash
docker pull minhle202/django-api
```

## Run

```bash
docker run --rm -p 8000:8000 minhle202/django-api
```

For production, supply your own secret key (and optionally a port):

```bash
docker run --rm -p 8000:8000 \
  -e SECRET_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(50))')" \
  -e PORT=8000 \
  minhle202/django-api
```

## Try it

```bash
curl http://localhost:8000/
curl http://localhost:8000/health
curl "http://localhost:8000/api/hello?name=Minh"
```

```json
{"name": "django-api", "version": "1.0.0", "endpoints": ["/", "/health", "/api/hello"]}
{"status": "ok", "uptime": 12.34}
{"message": "Hello, Minh!"}
```

## Endpoints

| Method | Path               | Description                                  | Example response                                            |
| ------ | ------------------ | -------------------------------------------- | ---------------------------------------------------------- |
| GET    | `/`                | Service metadata                             | `{"name":"django-api","version":"1.0.0","endpoints":[...]}`|
| GET    | `/health`          | Liveness probe + uptime (seconds)            | `{"status":"ok","uptime":12.34}`                           |
| GET    | `/api/hello?name=` | Greeting; `name` defaults to `world`         | `{"message":"Hello, world!"}`                              |

## What's inside

- **Python 3.12-slim** base image.
- **Django 5 + Gunicorn** (2 workers × 4 threads).
- Plain Django **`JsonResponse` views (no DRF)** — minimal `INSTALLED_APPS`,
  no database.
- **Multi-stage build**: dependencies installed into a `venv` in a builder
  stage, copied into a clean runtime stage.
- Runs as a **non-root** user (`appuser`, uid `10001`).
- Built-in **`HEALTHCHECK`** hitting `/health`.
- Hardened defaults: **`DEBUG=False`**, `SECRET_KEY` read from the
  environment (with a dev-only fallback).

## Tags

- `latest` — multi-arch manifest covering **linux/amd64** and **linux/arm64**.

## License

[MIT](LICENSE) © 2026 Lê Đức Minh
