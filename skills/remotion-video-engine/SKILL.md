---
name: remotion-video-engine
description: >
  Programmatic video creation and dynamic motion graphics using Remotion (React + TypeScript).
  Use when: create video with code, generate dynamic marketing videos, render Instagram Reels / TikTok / YouTube Shorts,
  automate personalized client video proposals, dynamic typography animations, audio-reactive waveforms, or programmatic product teasers.
compatibility: Requires Node.js 18+ and @remotion/cli or Remotion React templates.
---

# Remotion Programmatic Video Engine 🎬

Render high-conversion marketing videos, Instagram Reels, TikTok teasers, client onboarding demos, and dynamic motion graphics programmatically using React, TypeScript, and Remotion.

Directly powers automated social client acquisition (`Postiz`, `instaviral_ai_commenter`, Jasper SaaS portfolio demos).

---

## ⚡ Core Architecture & Capabilities

```
React Component Tree (TSX)  ──►  Remotion Player / Preview (Vite)
            │
            ▼
Remotion Engine (@remotion/bundler)  ──►  Chromium Headless Render  ──►  MP4 / ProRes / WebM Video
```

1. **Client Acquisition & Cold Outreach Videos**: Render dynamic videos with customized client names, website audits, metrics, and animated logos on the fly.
2. **Social Media Automation**: Auto-generate 9:16 vertical Reels/Shorts for Instagram & TikTok directly from Markdown / JSON scripts.
3. **Dynamic Motion Graphics**: Spring physics (`spring()`), timeline interpolations (`interpolate()`), soundwave visualizers, and typography reveals.

---

## 🛠️ CLI Quickstart & Setup

### 1. Initialize a Remotion Project
```bash
npx create-video@latest my-video
# Or using specific templates:
npx create-video@latest --template=tiktok
```

### 2. Preview & Interactive Studio
```bash
npm run dev
# Opens local Remotion preview studio on http://localhost:3000
```

### 3. Programmatic Headless Rendering
```bash
# Render composition 'ClientPitch' to MP4
npx remotion render src/index.ts ClientPitch out/pitch_video.mp4 --props='{"clientName":"Alpha Corp","savings":"45%"}'
```

---

## 💎 Production Recipes for High-Conversion Client Videos

### Recipe 1: 9:16 Vertical Reel with Kinetic Typography (`Composition.tsx`)
```tsx
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";

interface PitchProps {
  headline: string;
  subtext: string;
  metric: string;
}

export const ClientPitchVideo: React.FC<PitchProps> = ({ headline, subtext, metric }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Smooth entrance spring
  const scale = spring({
    frame,
    fps,
    config: { damping: 12, mass: 0.5, stiffness: 100 },
  });

  const opacity = interpolate(frame, [0, 20], [0, 1], {
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: "#050608",
        color: "#ffffff",
        justifyContent: "center",
        alignItems: "center",
        fontFamily: "'Inter', sans-serif",
        padding: "40px",
      }}
    >
      {/* Background Glow */}
      <div
        style={{
          position: "absolute",
          width: 500,
          height: 500,
          borderRadius: "50%",
          background: "radial-gradient(circle, rgba(99,102,241,0.25) 0%, rgba(0,0,0,0) 70%)",
          filter: "blur(60px)",
        }}
      />

      <div style={{ transform: `scale(${scale})`, opacity, textAlign: "center", zIndex: 10 }}>
        <span
          style={{
            fontSize: 28,
            color: "#6366f1",
            textTransform: "uppercase",
            letterSpacing: 4,
            fontWeight: 700,
          }}
        >
          {subtext}
        </span>
        <h1
          style={{
            fontSize: 72,
            fontWeight: 900,
            marginTop: 20,
            marginBottom: 20,
            lineHeight: 1.1,
          }}
        >
          {headline}
        </h1>
        <div
          style={{
            fontSize: 96,
            fontWeight: 900,
            color: "#10b981",
            textShadow: "0 0 30px rgba(16,185,129,0.4)",
          }}
        >
          {metric}
        </div>
      </div>
    </AbsoluteFill>
  );
};
```

---

## 🚀 Postiz & Social Automation Pipeline Integration

Combine `Remotion` with `Postiz` CLI for 100% autonomous video marketing:

```bash
# 1. Render automated promo clip
npx remotion render src/index.ts JasperSaaSPromo out/promo.mp4

# 2. Upload to Postiz CDN
MEDIA_ID=$(postiz upload out/promo.mp4 | grep -o 'media_[a-z0-9]*')

# 3. Auto-publish to Instagram Reels, TikTok & YouTube Shorts
postiz posts:create --content "🚀 Discover the new Autonomous AI agent stack built for 2026. #AI #SaaS #Automation" --media $MEDIA_ID
```
