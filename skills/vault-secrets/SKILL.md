---
name: vault-secrets
description: Secure secrets management, API key rotation, and encrypted credential storage using HashiCorp Vault. Use when implementing Zero-Secret-Leakage architectures, storing Telegram bot tokens, payment gateway credentials (Payme/Click/Uzum), and database passwords securely.
---

# HashiCorp Vault Skill (Zero-Secret-Leakage Secrets Engine)

Eliminates hardcoded API credentials, Telegram bot tokens, and database passwords by injecting secrets dynamically at runtime through encrypted KV engines.

## 1. Vault Server (Docker Compose)

```yaml
version: "3.8"

services:
  vault:
    image: hashicorp/vault:1.15
    container_name: vault
    restart: unless-stopped
    ports:
      - "127.0.0.1:8200:8200"
    environment:
      VAULT_DEV_ROOT_TOKEN_ID: ${VAULT_ROOT_TOKEN}
      VAULT_DEV_LISTEN_ADDRESS: "0.0.0.0:8200"
    cap_add:
      - IPC_LOCK
    volumes:
      - vault_data:/vault/file
    networks:
      - app_network

volumes:
  vault_data:

networks:
  app_network:
    driver: bridge
```

---

## 2. Python (HVAC) Integration (`core/secrets.py`)

### Package
```bash
pip install hvac
```

### Dynamic Secret Fetcher
```python
import os
import hvac

class VaultManager:
    def __init__(self):
        self.url = os.getenv("VAULT_ADDR", "http://127.0.0.1:8200")
        self.token = os.getenv("VAULT_TOKEN")
        self.client = hvac.Client(url=self.url, token=self.token)

    def get_secret(self, path: str, mount_point: str = "secret") -> dict:
        """Fetch credentials from KV v2 engine."""
        read_response = self.client.secrets.kv.v2.read_secret_version(
            path=path,
            mount_point=mount_point,
        )
        return read_response["data"]["data"]

# Usage:
# vault = VaultManager()
# bot_config = vault.get_secret("telegram/bot")
# BOT_TOKEN = bot_config["token"]
```

---

## 3. Best Practices (Jasper Production Standards)
1. **Never commit `.env` containing production master tokens**: Only store `VAULT_ADDR` and temporary AppRole credentials; all real database and payment secrets stay encrypted inside Vault.
2. **Short-Lived Leases**: Use short TTLs for database dynamic credentials so compromised tokens expire automatically.
3. **Audit Logging**: Enable Vault audit logs to record every secret access with timestamps.
