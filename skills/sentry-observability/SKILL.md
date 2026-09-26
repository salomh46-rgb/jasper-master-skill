---
name: sentry-observability
description: Sentry error tracking, distributed tracing, and real-time crash reporting skill. Use when instrumenting Python (FastAPI, Celery, Aiogram), Node.js, and Next.js applications with automated exception capturing, performance tracing, and sensitive data (PII/secrets) redaction.
---

# Sentry Observability Skill (Error Tracking & Crash Defense)

Instruments applications with production error monitoring, crash alerts, and distributed tracing while strictly enforcing **Zero-Secret-Leakage**.

## 1. Python & FastAPI Integration

### Package
```bash
pip install sentry-sdk[fastapi]
```

### Setup with Secret Masking (`core/sentry.py`)
```python
import os
import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.redis import RedisIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration

def before_send_filter(event, hint):
    """Jasper Standard: Redact sensitive tokens and passwords before dispatch."""
    if "request" in event and "headers" in event["request"]:
        headers = event["request"]["headers"]
        for sensitive_key in ["authorization", "x-telegram-init-data", "cookie"]:
            if sensitive_key in headers:
                headers[sensitive_key] = "[FILTERED]"
    return event

def init_sentry():
    dsn = os.getenv("SENTRY_DSN")
    if not dsn:
        return

    sentry_sdk.init(
        dsn=dsn,
        environment=os.getenv("ENVIRONMENT", "production"),
        traces_sample_rate=0.2, # 20% performance traces to save quota
        profiles_sample_rate=0.1,
        integrations=[
            FastApiIntegration(transaction_style="endpoint"),
            RedisIntegration(),
            SqlalchemyIntegration(),
        ],
        before_send=before_send_filter,
        send_default_pii=False,
    )
```

---

## 2. Telegram Bot (Aiogram 3) Exception Interceptor

```python
from aiogram import Dispatcher
from aiogram.types import ErrorEvent
import sentry_sdk

def register_sentry_error_handler(dp: Dispatcher):
    @dp.error()
    async def global_error_handler(event: ErrorEvent):
        with sentry_sdk.push_scope() as scope:
            if event.update.message and event.update.message.from_user:
                user = event.update.message.from_user
                scope.set_user({"id": str(user.id), "username": user.username})
            scope.set_extra("update_id", event.update.update_id)
            sentry_sdk.capture_exception(event.exception)
        
        # User-friendly fallback in Uzbek
        if event.update.message:
            await event.update.message.answer(
                "Kechirasiz, tizimda vaqtinchalik texnik xatolik yuz berdi. "
                "Muammo mutaxassislarimizga yuborildi."
            )
```

---

## 3. Next.js (App Router) Integration

### Install
```bash
npx @sentry/wizard@latest -i nextjs
```

### Client / Server Config (`sentry.server.config.ts`)
```typescript
import * as Sentry from "@sentry/nextjs";

Sentry.init({
  dsn: process.env.NEXT_PUBLIC_SENTRY_DSN,
  tracesSampleRate: 0.1,
  environment: process.env.NODE_ENV,
  beforeSend(event) {
    // Redact authorization or token parameters
    if (event.request?.headers) {
      delete event.request.headers["authorization"];
    }
    return event;
  },
});
```

---

## 4. Best Practices (Jasper Production Standards)
1. **Never send Telegram Bot Tokens or Payment API Keys** to Sentry breadcrumbs or tags.
2. **Use sample rates** (`0.1` or `0.2`) for high-traffic endpoints to prevent hitting free tier quota exhaustion.
3. **Group by Root Cause**: Use custom tags (`scope.set_tag("module", "payment_webhook")`) to instantly isolate the failure domain.
