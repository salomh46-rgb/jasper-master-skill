---
name: postiz
description: >
  Autonomous multi-channel social media marketing, scheduling, media uploading, and analytics
  via Postiz CLI. Use when: create social media post, schedule post, publish to Instagram,
  TikTok, YouTube, LinkedIn, X, Telegram, upload media, or fetch social media analytics.
compatibility: Requires postiz CLI installed (npm install -g postiz).
---

# Postiz Social Media Automation Engine 📢

Automate multi-platform publishing across 28+ channels (Instagram, TikTok, YouTube, LinkedIn, X/Twitter, Reddit, Telegram) directly from Antigravity and automated marketing workflows (`instashop_ai_automation`, `instaviral_ai_commenter`).

---

## ⚡ Core CLI Commands Reference

| Command | Action | Description |
| :--- | :--- | :--- |
| `postiz auth:status` | Check Auth | Verifies OAuth2 or `POSTIZ_API_KEY` connection. |
| `postiz integrations:list` | List Channels | Displays all connected social media accounts/channels. |
| `postiz upload <file>` | Upload Asset | Uploads image or video to Postiz CDN, returning media ID. |
| `postiz posts:create` | Create Post | Creates or schedules a multi-platform post. |
| `postiz posts:list` | List Posts | Displays drafts, scheduled posts, and published campaigns. |
| `postiz analytics:platform <id>` | Channel Metrics | Fetches engagement, reach, and performance stats. |
| `postiz analytics:post <id>` | Post Metrics | Fetches impressions, likes, and comment stats for a post. |

---

## 🔒 Authentication

1. **OAuth2 Flow (Interactive)**:
   ```bash
   postiz auth:login
   ```
2. **API Key Flow (Autonomous Headless)**:
   Set in `.env`:
   ```bash
   POSTIZ_API_KEY=your_postiz_api_key
   ```

---

## 🎯 Production Workflow for Jasper Marketing Agents

### 1. Upload Media
```bash
postiz upload "assets/banner.png"
```

### 2. Schedule Multi-Platform Post
```bash
postiz posts:create --content "⚡ New Jasper AI systems release! Check it out." --schedule "2026-09-27T10:00:00Z"
```

### 3. Verify Publication & Metrics
```bash
postiz posts:list
postiz analytics:post <POST_ID>
```
