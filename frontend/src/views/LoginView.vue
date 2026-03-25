<template>
  <div class="auth-page">
    <div class="auth-card">
      <h1 class="auth-title">Never<span class="accent">Late</span></h1>
      <h2 class="auth-subtitle">Welcome back</h2>

      <form @submit.prevent="handleLogin" class="auth-form">
        <div class="form-group">
          <label>Email</label>
          <input v-model="email" type="email" placeholder="you@example.com" required />
        </div>
        <div class="form-group">
          <label>Password</label>
          <input v-model="password" type="password" placeholder="Enter your password" required />
        </div>

        <p v-if="authError" class="auth-error">{{ authError }}</p>

        <button type="submit" class="btn btn-primary btn-full" :disabled="authLoading">
          {{ authLoading ? 'Logging in...' : 'Log In' }}
        </button>
      </form>

      <p class="auth-switch">
        Don't have an account? <a v-if="isDesktop" href="http://localhost:8080/signup" target="_blank">Sign up on the website</a>
        <router-link v-else to="/signup">Sign up</router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAuth } from '../composables/useAuth'
import { isTauri } from '../utils/platform'

const router = useRouter()
const { login, authError, authLoading } = useAuth()
const isDesktop = computed(() => isTauri())

const email    = ref('')
const password = ref('')

async function handleLogin() {
  const success = await login(email.value, password.value)
  if (success) {
    router.push(isDesktop.value ? '/dashboard' : '/')
  }
}
</script>

<style scoped>
.auth-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}
.auth-card {
  width: 100%;
  max-width: 400px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 2.5rem;
}
.auth-title {
  font-size: 1.6rem;
  font-weight: 800;
  letter-spacing: -0.5px;
  margin-bottom: 0.25rem;
}
.accent { color: var(--primary-h); }
.auth-subtitle {
  font-size: 1.1rem;
  color: var(--text-muted);
  margin-bottom: 2rem;
  font-weight: 400;
}
.auth-form { display: flex; flex-direction: column; gap: 1rem; }
.form-group { display: flex; flex-direction: column; gap: 0.4rem; }
.form-group label { font-size: 0.8rem; color: var(--text-muted); font-weight: 500; }
.form-group input {
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 0.7rem 0.9rem;
  color: var(--text);
  font-size: 0.9rem;
  font-family: inherit;
}
.form-group input:focus { outline: none; border-color: var(--primary); }
.auth-error {
  color: var(--danger);
  font-size: 0.85rem;
  background: rgba(248,113,113,0.1);
  padding: 0.5rem 0.75rem;
  border-radius: 6px;
}
.btn {
  border: none;
  border-radius: 8px;
  padding: 0.75rem;
  font-weight: 600;
  font-size: 0.95rem;
  cursor: pointer;
  transition: all 0.15s;
}
.btn-primary { background: var(--primary); color: #fff; }
.btn-primary:hover:not(:disabled) { background: var(--primary-h); }
.btn-primary:disabled { opacity: 0.5; cursor: not-allowed; }
.btn-full { width: 100%; }
.auth-switch {
  text-align: center;
  margin-top: 1.5rem;
  font-size: 0.85rem;
  color: var(--text-muted);
}
.auth-switch a { color: var(--primary-h); font-weight: 600; }
</style>
