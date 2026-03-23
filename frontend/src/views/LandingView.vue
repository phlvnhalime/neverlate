<template>
  <div class="landing">

    <!-- ── NAV ─────────────────────────────────────────────── -->
    <nav class="nav">
      <div class="nav-inner">
        <span class="logo">Never<span class="accent">Late</span></span>
        <div class="nav-links">
          <a href="#features">Features</a>
          <a href="#download">Download</a>
        </div>
      </div>
    </nav>

    <!-- ── HERO ───────────────────────────────────────────── -->
    <section class="hero">
      <div class="hero-badge">✦ Sync all your calendars in one place</div>
      <h1 class="hero-title">
        Never miss<br />
        <span class="gradient-text">what matters.</span>
      </h1>
      <p class="hero-sub">
        NeverLate brings your Google, Outlook &amp; Apple calendars together
        with a smart to-do list — so you always know what's next.
      </p>
      <div class="hero-actions">
        <a href="#download" class="btn btn-outline btn-lg">Download the App</a>
      </div>

      <!-- floating calendar cards -->
      <div class="hero-cards">
        <div class="card-float card-google">
          <span class="card-icon">📅</span>
          <div>
            <div class="card-title">Google Calendar</div>
            <div class="card-sub">3 events today</div>
          </div>
        </div>
        <div class="card-float card-apple">
          <span class="card-icon">🍎</span>
          <div>
            <div class="card-title">Apple Calendar</div>
            <div class="card-sub">2 reminders</div>
          </div>
        </div>
        <div class="card-float card-outlook">
          <span class="card-icon">📧</span>
          <div>
            <div class="card-title">Outlook</div>
            <div class="card-sub">1 meeting</div>
          </div>
        </div>
      </div>
    </section>

    <!-- ── FEATURES ───────────────────────────────────────── -->
    <section class="features" id="features">
      <h2 class="section-title">Everything you need</h2>
      <p class="section-sub">One app. All your calendars. Zero excuses.</p>
      <div class="features-grid">
        <div class="feature-card" v-for="f in features" :key="f.icon">
          <div class="feature-icon">{{ f.icon }}</div>
          <h3>{{ f.title }}</h3>
          <p>{{ f.desc }}</p>
        </div>
      </div>
    </section>

    <!-- ── DOWNLOAD ───────────────────────────────────────── -->
    <section class="download" id="download">
      <div class="download-inner">
        <h2>Take it everywhere</h2>
        <p>Available only for macOS</p>
        <div class="download-buttons">
          <a class="store-btn" href="/downloads/NeverLate-mac.dwg" download>
            <span class="store-icon">🍎</span>
            <div>
              <div class="store-label">Download for macOS</div>
              <div class="store-name">macOS (.dmg)</div>
            </div>
          </a>
        </div>
      </div>
    </section>

    <!-- ── FOOTER ─────────────────────────────────────────── -->
    <footer class="footer">
      <span class="logo">Never<span class="accent">Late</span></span>
      <span class="footer-copy">© 2026 NeverLate. Built with FastAPI + Vue.js</span>
    </footer>

  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

const features = [
  {
    icon: '🔄',
    title: 'Calendar Sync',
    desc: 'Connect Google, Apple and Outlook calendars. All events in one unified view.',
  },
  {
    icon: '✅',
    title: 'Smart To-Do List',
    desc: 'Create tasks linked to calendar events. Mark them done and stay on top.',
  },
  {
    icon: '🔔',
    title: 'Smart Reminders',
    desc: 'Get notified before it is too late. Never be late again.',
  },
  {
    icon: '🔐',
    title: 'Secure Login',
    desc: 'Sign in with Google, Apple or Microsoft. Your data stays yours.',
  },
  {
    icon: '📱',
    title: 'Works Everywhere',
    desc: 'Web app, iOS, and Android — your tasks follow you everywhere.',
  },
  {
    icon: '⚡',
    title: 'Instant Sync',
    desc: 'Changes sync across all your devices in real time.',
  },
]
</script>

<style scoped>
.landing {
  min-height: 100vh;
}

/* ── NAV ── */
.nav {
  position: sticky;
  top: 0;
  z-index: 100;
  backdrop-filter: blur(16px);
  background: rgba(15, 23, 42, 0.85);
  border-bottom: 1px solid var(--border);
}
.nav-inner {
  max-width: 1100px;
  margin: 0 auto;
  padding: 1rem 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.logo {
  font-size: 1.4rem;
  font-weight: 800;
  letter-spacing: -0.5px;
}
.accent { color: var(--primary-h); }
.nav-links {
  display: flex;
  align-items: center;
  gap: 2rem;
  font-size: 0.9rem;
  color: var(--text-muted);
}
.nav-links a:hover { color: var(--text); }

/* ── BUTTONS ── */
.btn {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  transition: all 0.2s;
}
.btn-primary {
  background: var(--primary);
  color: #fff;
  padding: 0.55rem 1.2rem;
}
.btn-primary:hover { background: var(--primary-h); transform: translateY(-1px); }
.btn-outline {
  background: transparent;
  color: var(--text);
  border: 1px solid var(--border);
  padding: 0.55rem 1.2rem;
}
.btn-outline:hover { background: var(--bg-card); }
.btn-sm { font-size: 0.85rem; }
.btn-lg { padding: 0.85rem 2rem; font-size: 1rem; border-radius: 10px; }

/* ── HERO ── */
.hero {
  max-width: 1100px;
  margin: 0 auto;
  padding: 6rem 2rem 4rem;
  text-align: center;
  position: relative;
}
.hero-badge {
  display: inline-block;
  background: rgba(99,102,241,0.15);
  border: 1px solid rgba(99,102,241,0.3);
  color: var(--primary-h);
  padding: 0.35rem 1rem;
  border-radius: 999px;
  font-size: 0.85rem;
  font-weight: 500;
  margin-bottom: 2rem;
}
.hero-title {
  font-size: clamp(2.8rem, 7vw, 5rem);
  font-weight: 800;
  line-height: 1.1;
  letter-spacing: -2px;
  margin-bottom: 1.5rem;
}
.gradient-text {
  background: linear-gradient(135deg, var(--primary), var(--accent));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.hero-sub {
  font-size: 1.15rem;
  color: var(--text-muted);
  max-width: 560px;
  margin: 0 auto 2.5rem;
  line-height: 1.7;
}
.hero-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 4rem;
}

/* ── FLOATING CARDS ── */
.hero-cards {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}
.card-float {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 0.9rem 1.25rem;
  box-shadow: var(--shadow);
  animation: float 4s ease-in-out infinite;
}
.card-float:nth-child(2) { animation-delay: 1.3s; }
.card-float:nth-child(3) { animation-delay: 2.6s; }
@keyframes float {
  0%, 100% { transform: translateY(0); }
  50%       { transform: translateY(-6px); }
}
.card-icon { font-size: 1.5rem; }
.card-title { font-size: 0.85rem; font-weight: 600; }
.card-sub   { font-size: 0.75rem; color: var(--text-muted); margin-top: 2px; }

/* ── FEATURES ── */
.features {
  background: var(--bg-card);
  padding: 5rem 2rem;
  text-align: center;
}
.section-title {
  font-size: 2.2rem;
  font-weight: 800;
  letter-spacing: -1px;
  margin-bottom: 0.5rem;
}
.section-sub {
  color: var(--text-muted);
  margin-bottom: 3rem;
  font-size: 1.05rem;
}
.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  max-width: 1100px;
  margin: 0 auto;
}
.feature-card {
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.75rem;
  text-align: left;
  transition: border-color 0.2s, transform 0.2s;
}
.feature-card:hover {
  border-color: var(--primary);
  transform: translateY(-3px);
}
.feature-icon { font-size: 2rem; margin-bottom: 1rem; }
.feature-card h3 { font-size: 1rem; font-weight: 700; margin-bottom: 0.5rem; }
.feature-card p  { font-size: 0.88rem; color: var(--text-muted); line-height: 1.6; }

/* ── DOWNLOAD ── */
.download {
  padding: 6rem 2rem;
  text-align: center;
}
.download-inner { max-width: 700px; margin: 0 auto; }
.download h2 { font-size: 2rem; font-weight: 800; margin-bottom: 0.75rem; letter-spacing: -1px; }
.download p  { color: var(--text-muted); margin-bottom: 2.5rem; font-size: 1.05rem; }
.download-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}
.store-btn {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 0.9rem 1.5rem;
  transition: all 0.2s;
  min-width: 170px;
}
.store-btn:hover {
  border-color: var(--primary);
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(99,102,241,0.2);
}
.store-web { border-color: var(--accent); }
.store-web:hover { border-color: var(--accent); box-shadow: 0 8px 24px rgba(34,211,238,0.2); }
.store-icon { font-size: 1.6rem; }
.store-label { font-size: 0.7rem; color: var(--text-muted); }
.store-name  { font-size: 0.95rem; font-weight: 700; }

/* ── FOOTER ── */
.footer {
  border-top: 1px solid var(--border);
  padding: 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1100px;
  margin: 0 auto;
  flex-wrap: wrap;
  gap: 1rem;
}
.footer-copy { font-size: 0.8rem; color: var(--text-muted); }
</style>
