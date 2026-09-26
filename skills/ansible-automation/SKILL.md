---
name: ansible-automation
description: Server provisioning, configuration management, and VPS hardening skill using Ansible. Use when setting up new Linux/Ubuntu servers, configuring firewalls (UFW), installing Docker & Docker Compose, managing Nginx SSL certificates, and automating server deployments.
---

# Ansible Automation Skill (1-Click VPS Provisioning & Hardening)

Ansible provides simple, agentless, push-based server provisioning over secure SSH connections.

## 1. Inventory Configuration (`hosts.ini`)

```ini
[production]
server1 ansible_host=YOUR_SERVER_IP ansible_user=root ansible_ssh_private_key_file=~/.ssh/id_rsa

[production:vars]
ansible_python_interpreter=/usr/bin/python3
timezone=Asia/Tashkent
deploy_user=jasper
```

---

## 2. Master Server Setup Playbook (`setup-server.yml`)

```yaml
---
- name: Provision Production Ubuntu VPS
  hosts: production
  become: true
  tasks:
    - name: Set Timezone to Asia/Tashkent
      community.general.timezone:
        name: "{{ timezone }}"

    - name: Update apt packages
      apt:
        update_cache: yes
        upgrade: dist
        autoremove: yes

    - name: Install essential utilities
      apt:
        name:
          - curl
          - git
          - ufw
          - fail2ban
          - htop
          - unattended-upgrades
        state: present

    - name: Create non-root deployer user
      user:
        name: "{{ deploy_user }}"
        shell: /bin/bash
        groups: sudo
        append: yes

    - name: Configure UFW firewall
      ufw:
        rule: allow
        port: "{{ item }}"
        proto: tcp
      loop:
        - '22'
        - '80'
        - '443'

    - name: Enable UFW
      ufw:
        state: enabled
        default: deny

    - name: Install Docker & Docker Compose plugin
      shell: |
        curl -fsSL https://get.docker.com | sh
        usermod -aG docker {{ deploy_user }}
      args:
        creates: /usr/bin/docker

    - name: Ensure Docker service is running
      systemd:
        name: docker
        state: started
        enabled: yes

    - name: Configure Fail2ban for SSH defense
      copy:
        dest: /etc/fail2ban/jail.local
        content: |
          [sshd]
          enabled = true
          port = 22
          maxretry = 5
          bantime = 1d
          findtime = 10m
      notify: Restart Fail2ban

  handlers:
    - name: Restart Fail2ban
      systemd:
        name: fail2ban
        state: restarted
```

---

## 3. Running the Playbook
```bash
ansible-playbook -i hosts.ini setup-server.yml
```

---

## 4. Best Practices (Jasper Production Standards)
1. **Never store SSH passwords in plaintext**: Always use SSH key pairs (`~/.ssh/id_rsa`).
2. **Idempotency Invariant**: Ensure playbooks can be run multiple times safely without breaking existing services (`args: creates: ...`).
3. **Always enable `fail2ban`**: Blocks malicious brute-force attempts on port 22 automatically.
