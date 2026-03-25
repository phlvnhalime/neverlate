<template>
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
</template>

<style scoped>
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

.btn {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  transition: all 0.2s;
}
.btn-outline {
  background: transparent;
  color: var(--text);
  border: 1px solid var(--border);
  padding: 0.55rem 1.2rem;
}
.btn-outline:hover { background: var(--bg-card); }
.btn-lg { padding: 0.85rem 2rem; font-size: 1rem; border-radius: 10px; }

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
</style>
