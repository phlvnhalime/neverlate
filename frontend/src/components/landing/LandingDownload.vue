<template>
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
</template>

<style scoped>
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
.store-icon { font-size: 1.6rem; }
.store-label { font-size: 0.7rem; color: var(--text-muted); }
.store-name  { font-size: 0.95rem; font-weight: 700; }
</style>
