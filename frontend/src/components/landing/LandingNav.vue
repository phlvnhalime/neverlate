<template>
  <nav class="nav">
    <div class="nav-inner">
      <span class="logo">Never<span class="accent">Late</span></span>
      <div class="nav-links">
        <a href="#features">Features</a>
        <a href="#download">Download</a>
        <router-link to="/login" class="nav-btn nav-btn-outline">Log in</router-link>
        <router-link to="/signup" class="nav-btn nav-btn-primary">Sign Up</router-link>
      </div>
    </div>
  </nav>
</template>

<style scoped>
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
  gap: 1.5rem;
  font-size: 0.9rem;
  color: var(--text-muted);
}
.nav-links a:hover { color: var(--text); }
.nav-btn {
  padding: 0.45rem 1rem;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.85rem;
  transition: all 0.15s;
}
.nav-btn-outline {
  border: 1px solid var(--border);
  color: var(--text);
}
.nav-btn-outline:hover { background: var(--bg-card); }
.nav-btn-primary {
  background: var(--primary);
  color: #fff;
}
.nav-btn-primary:hover { background: var(--primary-h); }
</style>
