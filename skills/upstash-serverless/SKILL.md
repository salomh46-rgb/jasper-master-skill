---
name: upstash-serverless
description: >
  Serverless Redis, QStash background messaging queues, Sliding-Window Rate Limiting, and Vector search via Upstash.
  Use when: serverless redis, rate limiting API endpoints, protecting Telegram bots from spam, queueing background client tasks,
  distributed locking, caching external API responses, or vector embeddings for fast semantic lead triage.
compatibility: Works with Python (upstash-redis) and Node.js/TypeScript (@upstash/redis, @upstash/ratelimit, @upstash/qstash).
---

# Upstash Serverless Ecosystem & Rate Limiting ⚡

Production-grade serverless data layer for high-throughput FastAPI APIs, Next.js applications, and Telegram bots (`@Ovozli_SavdoBOT`, `@DentaMedKlinika_bot`).

Provides instant sub-millisecond in-memory caching, DDOS/spam protection via sliding-window rate limiting, and durable background task queuing via QStash.

---

## 🔑 Environment Variables (.env)
```bash
UPSTASH_REDIS_REST_URL="https://xxx.upstash.io"
UPSTASH_REDIS_REST_TOKEN="your_upstash_redis_token"
QSTASH_TOKEN="your_qstash_token"
```

---

## 🛡️ 1. Ultra-Resilient API Rate Limiting (Next.js / TypeScript)

Protect client-facing landing pages and API endpoints from abuse with sliding-window rate limiting:

```typescript
import { Ratelimit } from "@upstash/ratelimit";
import { Redis } from "@upstash/redis";

const redis = Redis.fromEnv();

// Allow 10 requests per 10 seconds per IP
export const ratelimit = new Ratelimit({
  redis,
  limiter: Ratelimit.slidingWindow(10, "10 s"),
  analytics: true,
  prefix: "@upstash/ratelimit:jasper",
});

// Middleware usage:
export async function verifyRateLimit(req: Request, clientIp: string) {
  const { success, limit, remaining, reset } = await ratelimit.limit(clientIp);
  if (!success) {
    return new Response(JSON.stringify({ error: "Too many requests. Please slow down." }), {
      status: 429,
      headers: {
        "X-RateLimit-Limit": limit.toString(),
        "X-RateLimit-Remaining": remaining.toString(),
        "X-RateLimit-Reset": reset.toString(),
      },
    });
  }
  return null;
}
```

---

## 🐍 2. Python FastAPI & Telegram Bot Integration

### Fast Distributed Caching & Anti-Spam Lock
```python
from upstash_redis import Redis
import os

redis = Redis(
    url=os.getenv("UPSTASH_REDIS_REST_URL"),
    token=os.getenv("UPSTASH_REDIS_REST_TOKEN")
)

# 1. Cache CRM client lookup (TTL: 1 hour)
def get_cached_client(client_id: str):
    cache_key = f"client:{client_id}"
    cached_data = redis.get(cache_key)
    if cached_data:
        return cached_data
    
    # Fetch from database...
    data = {"id": client_id, "status": "active", "tier": "enterprise"}
    redis.set(cache_key, data, ex=3600)
    return data

# 2. Concurrency Lock (Prevents double payment clicks)
def acquire_payment_lock(order_id: str) -> bool:
    lock_key = f"lock:payment:{order_id}"
    # Set if not exists with 15-second expiry
    return bool(redis.set(lock_key, "locked", nx=True, ex=15))
```

---

## 📬 3. QStash: Resilient Asynchronous Background Queues

Durable HTTP-based job queuing without managing background Celery/RabbitMQ workers:

```typescript
import { Client } from "@upstash/qstash";

const qstash = new Client({ token: process.env.QSTASH_TOKEN! });

// Schedule client proposal follow-up email after 24 hours
export async function scheduleLeadFollowUp(clientEmail: string) {
  await qstash.publishJSON({
    url: "https://your-api.com/api/leads/follow-up",
    body: { email: clientEmail },
    delay: 60 * 60 * 24, // 24 hours
    retries: 3,
  });
}
```

---

## 🚀 Client Acquisition Advantage
- **Zero Cold Start**: Sub-millisecond latency for international clients.
- **100% Uptime for Telegram Bots**: High-traffic spikes from viral marketing campaigns are absorbed seamlessly without database crashes.
