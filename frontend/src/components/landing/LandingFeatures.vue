<template>
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
</template>

<script setup>
const features = [
  { icon: '🔄', title: 'Calendar Sync',    desc: 'Connect Google, Apple and Outlook calendars. All events in one unified view.' },
  { icon: '✅', title: 'Smart To-Do List', desc: 'Create tasks linked to calendar events. Mark them done and stay on top.' },
  { icon: '🔔', title: 'Smart Reminders',  desc: 'Get notified before it is too late. Never be late again.' },
  { icon: '🔐', title: 'Secure Login',     desc: 'Sign in with Google, Apple or Microsoft. Your data stays yours.' },
  { icon: '📱', title: 'Works Everywhere', desc: 'Web app, iOS, and Android — your tasks follow you everywhere.' },
  { icon: '⚡', title: 'Instant Sync',     desc: 'Changes sync across all your devices in real time.' },
]
</script>

<style scoped>
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
</style>
