<template>
  <aside class="sidebar">
    <div class="sidebar-logo">Never<span class="accent">Late</span></div>

    <nav class="sidebar-nav">
      <button
        v-for="item in navItems"
        :key="item.label"
        class="nav-item"
        :class="{ active: activeSection === item.key }"
        @click="activeSection = item.key"
      >
        <span>{{ item.icon }}</span>
        {{ item.label }}
      </button>
    </nav>

    <div class="sidebar-calendars">
      <p class="sidebar-section-label">Calendars</p>
      <div v-for="cal in calendars" :key="cal.name" class="calendar-item">
        <span class="cal-dot" :style="{ background: cal.color }"></span>
        {{ cal.name }}
        <span class="cal-status" :class="cal.connected ? 'connected' : 'disconnected'">
          {{ cal.connected ? '✓' : '+ Connect' }}
        </span>
      </div>
    </div>

    <div class="sidebar-user" v-if="user">
      <span class="user-name">{{ user.first_name }}</span>
      <button class="logout-btn" @click="handleLogout">Log out</button>
    </div>
  </aside>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuth } from '../../composables/useAuth'

const router = useRouter()
const { user, logout } = useAuth()

const activeSection = ref('tasks')

function handleLogout() {
  logout()
  router.push('/login')
}

const navItems = [
  { key: 'tasks', icon: '✅', label: 'Tasks' },
  { key: 'calendar', icon: '📅', label: 'Calendar' },
  { key: 'settings', icon: '⚙️', label: 'Settings' },
]

const calendars = ref([
  { name: 'Google Calendar', color: '#4285f4', connected: false },
  { name: 'Apple Calendar',  color: '#ff3b30', connected: false },
  { name: 'Outlook',         color: '#0078d4', connected: false },
])
</script>

<style scoped>
.sidebar {
  width: 240px;
  min-width: 240px;
  background: var(--bg-card);
  border-right: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  padding: 1.5rem 1rem;
  gap: 0.5rem;
}
.sidebar-logo {
  font-size: 1.3rem;
  font-weight: 800;
  padding: 0.5rem 0.75rem 1.25rem;
  letter-spacing: -0.5px;
}
.accent { color: var(--primary-h); }
.sidebar-nav { display: flex; flex-direction: column; gap: 0.25rem; }
.nav-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.65rem 0.75rem;
  border-radius: 8px;
  border: none;
  background: transparent;
  color: var(--text-muted);
  font-size: 0.9rem;
  font-weight: 500;
  text-align: left;
  transition: all 0.15s;
}
.nav-item:hover, .nav-item.active {
  background: var(--bg-hover);
  color: var(--text);
}
.nav-item.active { color: var(--primary-h); }

.sidebar-section-label {
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--text-muted);
  padding: 1rem 0.75rem 0.5rem;
  font-weight: 600;
}
.sidebar-calendars { margin-top: 0.5rem; }
.calendar-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 0.75rem;
  font-size: 0.82rem;
  color: var(--text-muted);
}
.cal-dot {
  width: 8px; height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}
.cal-status { margin-left: auto; font-size: 0.75rem; }
.cal-status.connected    { color: var(--success); }
.cal-status.disconnected { color: var(--primary-h); cursor: pointer; }

.sidebar-user {
  margin-top: auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.75rem;
  border-top: 1px solid var(--border);
}
.user-name {
  font-size: 0.85rem;
  font-weight: 600;
}
.logout-btn {
  border: none;
  background: transparent;
  color: var(--text-muted);
  font-size: 0.78rem;
  cursor: pointer;
  transition: color 0.15s;
}
.logout-btn:hover { color: var(--danger); }
</style>
