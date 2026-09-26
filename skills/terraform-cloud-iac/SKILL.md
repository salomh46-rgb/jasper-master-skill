---
name: terraform-cloud-iac
description: Declarative cloud infrastructure automation skill using HashiCorp Terraform. Use when provisioning VPS instances (Hetzner, DigitalOcean, AWS, GCP), configuring cloud firewall rules, managing DNS records, and generating Infrastructure as Code (IaC) architectures.
---

# Terraform Cloud IaC Skill (Infrastructure as Code)

Terraform codifies cloud APIs into declarative configuration files, enabling version-controlled, reproducible cloud architectures.

## 1. Hetzner Cloud / DigitalOcean VPS Provisioning (`main.tf`)

```hcl
terraform {
  required_version = ">= 1.5.0"
  required_providers {
    hcloud = {
      source  = "hetznercloud/hcloud"
      version = "~> 1.45.0"
    }
    cloudflare = {
      source  = "cloudflare/cloudflare"
      version = "~> 4.0"
    }
  }
}

variable "hcloud_token" {
  type        = string
  sensitive   = true
  description = "Hetzner Cloud API Token"
}

variable "ssh_public_key" {
  type        = string
  description = "Public SSH key content"
}

provider "hcloud" {
  token = var.hcloud_token
}

# SSH Key
resource "hcloud_ssh_key" "default" {
  name       = "jasper-deploy-key"
  public_key = var.ssh_public_key
}

# Firewall
resource "hcloud_firewall" "web_firewall" {
  name = "web-production-firewall"

  # SSH
  rule {
    direction = "in"
    protocol  = "tcp"
    port      = "22"
    source_ips = ["0.0.0.0/0", "::/0"]
  }

  # HTTP & HTTPS
  rule {
    direction = "in"
    protocol  = "tcp"
    port      = "80"
    source_ips = ["0.0.0.0/0", "::/0"]
  }

  rule {
    direction = "in"
    protocol  = "tcp"
    port      = "443"
    source_ips = ["0.0.0.0/0", "::/0"]
  }
}

# VPS Server
resource "hcloud_server" "production_app" {
  name        = "jasper-prod-server"
  image       = "ubuntu-22.04"
  server_type = "cpx21" # 3 vCPU, 4GB RAM, 80GB NVMe
  location    = "fsn1"
  ssh_keys    = [hcloud_ssh_key.default.id]
  firewall_ids = [hcloud_firewall.web_firewall.id]

  labels = {
    environment = "production"
    owner       = "jasper"
  }
}

output "server_ip" {
  value       = hcloud_server.production_app.ipv4_address
  description = "Production Server IPv4 Address"
}
```

---

## 2. Terraform Workflow
```bash
# 1. Initialize providers
terraform init

# 2. Preview changes
terraform plan -var="hcloud_token=$HCLOUD_TOKEN" -var="ssh_public_key=$(cat ~/.ssh/id_rsa.pub)"

# 3. Apply infrastructure
terraform apply -auto-approve
```

---

## 3. Best Practices (Jasper Production Standards)
1. **Zero-Secret-Leakage in State**: Never hardcode API tokens in `.tf` files. Always pass via environment variables (`TF_VAR_hcloud_token` or `.tfvars` added to `.gitignore`).
2. **State Locking**: For production teams, use a remote backend with state locking (e.g., S3 + DynamoDB) to prevent concurrent state corruption.
3. **Plan Before Apply**: Always inspect `terraform plan` outputs before running `apply` to prevent accidental resource deletion.
