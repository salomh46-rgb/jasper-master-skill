---
name: docker-production
description: Production-grade Docker and Docker Compose orchestration skill. Use when creating Dockerfiles, docker-compose.yml, multi-stage builds, production volume mounts, PID/port cleanup, health checks, and Nginx reverse proxy setups for Python, Node.js, and Go applications.
---

# Docker Production Skill (Senior DevOps & Containerization)

Defines zero-regression containerization standards for high-performance microservices, Python backends, Next.js webapps, and background workers.

## 1. Multi-Stage Python (FastAPI / Celery) Dockerfile

```dockerfile
# syntax=docker/dockerfile:1.4
# Stage 1: Build stage
FROM python:3.11-slim-bookworm AS builder

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --user --no-warn-script-location -r requirements.txt

# Stage 2: Minimal Runtime stage
FROM python:3.11-slim-bookworm AS runner

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/home/appuser/.local/bin:$PATH" \
    TZ=Asia/Tashkent

# Security: Non-root user
RUN groupadd -g 1001 appgroup && \
    useradd -u 1001 -g appgroup -s /bin/bash -m appuser

COPY --from=builder /root/.local /home/appuser/.local
COPY --chown=appuser:appgroup . .

USER appuser

EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/api/health || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
```

---

## 2. Multi-Stage Next.js / Node.js Production Dockerfile

```dockerfile
# Stage 1: Dependencies
FROM node:20-alpine AS deps
WORKDIR /app
COPY package*.json ./
RUN npm ci

# Stage 2: Builder
FROM node:20-alpine AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
ENV NEXT_TELEMETRY_DISABLED=1
RUN npm run build

# Stage 3: Runner
FROM node:20-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production \
    NEXT_TELEMETRY_DISABLED=1 \
    PORT=3000

RUN addgroup --system --gid 1001 nodejs && \
    adduser --system --uid 1001 nextjs

COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs
EXPOSE 3000
CMD ["node", "server.js"]
```

---

## 3. Production `docker-compose.yml` (Stack with Postgres, Redis, Nginx)

```yaml
version: "3.8"

services:
  nginx:
    image: nginx:alpine
    restart: always
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./certbot/conf:/etc/letsencrypt:ro
      - ./certbot/www:/var/www/certbot:ro
    depends_on:
      - web
    networks:
      - app_network

  web:
    build:
      context: .
      dockerfile: Dockerfile
    restart: always
    environment:
      - DATABASE_URL=postgresql://appuser:${DB_PASSWORD}@postgres:5432/appdb
      - REDIS_URL=redis://redis:6379/0
      - TIMEZONE=Asia/Tashkent
    env_file:
      - .env
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    networks:
      - app_network

  postgres:
    image: postgres:16-alpine
    restart: always
    environment:
      POSTGRES_DB: appdb
      POSTGRES_USER: appuser
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U appuser -d appdb"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - app_network

  redis:
    image: redis:7-alpine
    restart: always
    command: ["redis-server", "--appendonly", "yes", "--requirepass", "${REDIS_PASSWORD}"]
    volumes:
      - redis_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 3s
      retries: 3
    networks:
      - app_network

volumes:
  postgres_data:
  redis_data:

networks:
  app_network:
    driver: bridge
```

---

## 4. Operational Clean-up Rules (Jasper Standards)
- **Port Conflict Fix (Windows / Linux):** Check port PID before starting:
  `netstat -ano | findstr :8000` -> `taskkill /PID <PID> /F`
- **Volume Hygiene:** Never store active SQLite or Postgres data inside ephemeral containers without named volumes.
- **Timezone Invariant:** Always enforce `TZ=Asia/Tashkent` across all containers.
