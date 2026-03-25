<template>
  <footer class="footer">
    <span class="logo">Never<span class="accent">Late</span></span>
    <span class="footer-copy">&copy; 2026 NeverLate. Built with FastAPI + Vue.js</span>
  </footer>
</template>

<style scoped>
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
.logo {
  font-size: 1.4rem;
  font-weight: 800;
  letter-spacing: -0.5px;
}
.accent { color: var(--primary-h); }
.footer-copy { font-size: 0.8rem; color: var(--text-muted); }
</style>
