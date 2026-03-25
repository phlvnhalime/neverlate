<template>
  <div class="main-header">
    <div>
      <h1 class="main-title">My Tasks</h1>
      <p class="main-sub">{{ todayString }}</p>
    </div>
    <div class="header-actions">
      <span class="api-badge" :class="apiStatus">
        {{ apiStatus === 'online' ? '● API Online' : '○ API Offline' }}
      </span>
      <button class="btn btn-primary" @click="showForm = !showForm">
        {{ showForm ? '✕ Cancel' : '+ New Task' }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { useTasks } from '../../composables/useTasks'

const { apiStatus, showForm, todayString } = useTasks()
</script>

<style scoped>
.main-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 2rem;
  flex-wrap: wrap;
  gap: 1rem;
}
.main-title { font-size: 1.75rem; font-weight: 800; letter-spacing: -0.5px; }
.main-sub   { color: var(--text-muted); font-size: 0.9rem; margin-top: 0.2rem; }
.header-actions { display: flex; align-items: center; gap: 1rem; }

.api-badge {
  font-size: 0.78rem;
  padding: 0.3rem 0.75rem;
  border-radius: 999px;
  font-weight: 600;
}
.api-badge.online  { background: rgba(52,211,153,0.15); color: var(--success); }
.api-badge.offline { background: rgba(248,113,113,0.15); color: var(--danger); }

.btn {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  border: none;
  border-radius: 8px;
  padding: 0.6rem 1.25rem;
  font-weight: 600;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.15s;
}
.btn-primary { background: var(--primary); color: #fff; }
.btn-primary:hover:not(:disabled) { background: var(--primary-h); transform: translateY(-1px); }
</style>
