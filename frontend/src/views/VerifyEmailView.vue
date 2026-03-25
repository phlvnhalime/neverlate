<template>
  <div class="auth-page">
    <div class="auth-card">
      <h1 class="auth-title">Never<span class="accent">Late</span></h1>
      <h2 class="auth-subtitle">Check your email</h2>
      <p class="auth-desc">
        We sent a 6-digit code to <strong>{{ email }}</strong>
      </p>

      <form @submit.prevent="handleVerify" class="auth-form">
        <div class="form-group">
          <label>Verification code</label>
          <input
            v-model="code"
            type="text"
            maxlength="6"
            placeholder="000000"
            class="code-input"
            required
          />
        </div>

        <p v-if="authError" class="auth-error">{{ authError }}</p>

        <button type="submit" class="btn btn-primary btn-full" :disabled="authLoading || code.length !== 6">
          {{ authLoading ? 'Verifying...' : 'Verify Email' }}
        </button>
      </form>

      <p class="auth-switch">
        Wrong email? <router-link to="/signup">Go back</router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuth } from '../composables/useAuth'

const route  = useRoute()
const router = useRouter()
const { verifyEmail, authError, authLoading } = useAuth()

const email = ref(route.query.email || '')
const code  = ref('')

async function handleVerify() {
  const success = await verifyEmail(email.value, code.value)
  if (success) {
    router.push('/')
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
  margin-bottom: 0.5rem;
  font-weight: 400;
}
.auth-desc {
  font-size: 0.9rem;
  color: var(--text-muted);
  margin-bottom: 1.5rem;
  line-height: 1.5;
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
.code-input {
  text-align: center;
  font-size: 1.5rem !important;
  letter-spacing: 8px;
  font-weight: 700;
}
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
