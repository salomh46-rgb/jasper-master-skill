---
name: prometheus-grafana
description: Production metrics monitoring, time-series analysis, and dashboard visualization skill using Prometheus, Grafana, and Node Exporter. Use when deploying infrastructure monitoring, instrumenting backend APIs with Prometheus metrics, or configuring alerting rules.
---

# Prometheus & Grafana Skill (Metrics & Observability Architecture)

Enables real-time system monitoring, server health telemetry, and API latency dashboards for production microservices and VPS instances.

## 1. 1-Click Docker Compose Monitoring Stack

```yaml
version: "3.8"

services:
  prometheus:
    image: prom/prometheus:v2.50.0
    container_name: prometheus
    restart: unless-stopped
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml:ro
      - prometheus_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--storage.tsdb.retention.time=30d'
    ports:
      - "127.0.0.1:9090:9090"
    networks:
      - monitoring

  node-exporter:
    image: prom/node-exporter:v1.7.0
    container_name: node-exporter
    restart: unless-stopped
    volumes:
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
      - /:/rootfs:ro
    command:
      - '--path.procfs=/host/proc'
      - '--path.rootfs=/rootfs'
      - '--path.sysfs=/host/sys'
    ports:
      - "127.0.0.1:9100:9100"
    networks:
      - monitoring

  grafana:
    image: grafana/grafana:10.3.3
    container_name: grafana
    restart: unless-stopped
    environment:
      - GF_SECURITY_ADMIN_USER=admin
      - GF_SECURITY_ADMIN_PASSWORD=${GRAFANA_ADMIN_PASSWORD}
      - GF_USERS_ALLOW_SIGN_UP=false
    volumes:
      - grafana_data:/var/lib/grafana
    ports:
      - "127.0.0.1:3001:3000"
    networks:
      - monitoring

volumes:
  prometheus_data:
  grafana_data:

networks:
  monitoring:
    driver: bridge
```

---

## 2. Prometheus Configuration (`prometheus.yml`)

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'node_exporter'
    static_configs:
      - targets: ['node-exporter:9100']

  - job_name: 'fastapi_backend'
    metrics_path: '/metrics'
    static_configs:
      - targets: ['web:8000']
```

---

## 3. Instrumenting FastAPI Backend (`metrics.py`)

### Package
```bash
pip install prometheus-fastapi-instrumentator
```

### Setup
```python
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

def init_metrics(app: FastAPI):
    # Exposes /metrics endpoint for Prometheus
    Instrumentator(
        should_group_status_codes=True,
        should_ignore_untemplated=True,
        excluded_handlers=["/metrics", "/api/health"],
    ).instrument(app).expose(app)
```

---

## 4. Curated Grafana Dashboards (IDs to import)
- **Node Exporter Full (System Metrics, CPU, RAM, Disk, Network):** Dashboard ID `1860`
- **FastAPI / HTTP Monitoring (Requests/sec, 4xx/5xx error rates, P95 latency):** Dashboard ID `16110`
- **Docker Container Metrics (cAdvisor):** Dashboard ID `14282`

---

## 5. Best Practices
1. **Never expose ports 9090, 9100, or 3000 directly to 0.0.0.0**: Bind them strictly to `127.0.0.1` and access via Nginx reverse proxy with HTTPS and basic auth, or through SSH tunneling (`ssh -L 3001:localhost:3001 user@server`).
2. **Set Retention**: Always limit TSDB retention (e.g. `--storage.tsdb.retention.time=30d`) to prevent VPS disk from filling up.
