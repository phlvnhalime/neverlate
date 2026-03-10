<template>
  <div class="app-shell">

    <!-- ── SIDEBAR ─────────────────────────────────────── -->
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
      <RouterLink to="/" class="back-link">← Back to site</RouterLink>
    </aside>

    <!-- ── MAIN ───────────────────────────────────────── -->
    <main class="main">

      <!-- Header -->
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

      <!-- Add Task Form -->
      <Transition name="slide">
        <div v-if="showForm" class="task-form">
          <h3 class="form-title">New Task</h3>
          <div class="form-grid">
            <div class="form-group form-full">
              <label>Title *</label>
              <input v-model="newTask.title" placeholder="What do you need to do?" />
            </div>
            <div class="form-group form-full">
              <label>Description</label>
              <input v-model="newTask.description" placeholder="Optional details..." />
            </div>
            <div class="form-group">
              <label>Start time (HHMM)</label>
              <input v-model.number="newTask.duration_start" type="number" placeholder="e.g. 900 = 9:00am" />
            </div>
            <div class="form-group">
              <label>End time (HHMM)</label>
              <input v-model.number="newTask.duration_end" type="number" placeholder="e.g. 1030 = 10:30am" />
            </div>
          </div>
          <div class="form-actions">
            <button class="btn btn-primary" @click="createTask" :disabled="!newTask.title">
              Save Task
            </button>
          </div>
        </div>
      </Transition>

      <!-- Stats bar -->
      <div class="stats-bar">
        <div class="stat">
          <span class="stat-num">{{ tasks.length }}</span>
          <span class="stat-label">Total</span>
        </div>
        <div class="stat">
          <span class="stat-num">{{ pendingTasks.length }}</span>
          <span class="stat-label">Pending</span>
        </div>
        <div class="stat">
          <span class="stat-num">{{ doneTasks.length }}</span>
          <span class="stat-label">Done</span>
        </div>
        <div class="stat">
          <span class="stat-num">{{ Math.round((doneTasks.length / (tasks.length || 1)) * 100) }}%</span>
          <span class="stat-label">Complete</span>
        </div>
      </div>

      <!-- Loading / Error -->
      <div v-if="loading" class="state-message">⏳ Loading tasks from API...</div>
      <div v-else-if="error" class="state-message state-error">
        ⚠️ {{ error }}
      </div>

      <!-- Task List -->
      <div v-else class="task-list">
        <div v-if="tasks.length === 0" class="empty-state">
          <div class="empty-icon">✅</div>
          <p>No tasks yet. Add your first one above!</p>
        </div>
        <div
          v-for="task in tasks"
          :key="task.id"
          class="task-card"
          :class="{ done: task.is_completed }"
        >
          <button class="task-check" @click="toggleTask(task)">
            {{ task.is_completed ? '✓' : '' }}
          </button>
          <div class="task-body">
            <p class="task-title">{{ task.title }}</p>
            <p v-if="task.description" class="task-desc">{{ task.description }}</p>
            <div class="task-meta">
              <span v-if="task.duration_start">
                🕐 {{ formatTime(task.duration_start) }} – {{ formatTime(task.duration_end) }}
              </span>
              <span v-if="task.provider" class="task-provider">📅 {{ task.provider }}</span>
            </div>
          </div>
          <button class="task-delete" @click="deleteTask(task.id)" title="Delete">✕</button>
        </div>
      </div>

    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import axios from 'axios'

// ── API base URL — calls YOUR FastAPI backend ──────────────────────
const API = 'http://localhost:8000'

// ── State ──────────────────────────────────────────────────────────
const tasks      = ref([])
const loading    = ref(true)
const error      = ref(null)
const showForm   = ref(false)
const apiStatus  = ref('offline')
const activeSection = ref('tasks')

const newTask = ref({ title: '', description: '', duration_start: 900, duration_end: 1000 })

// ── Computed ───────────────────────────────────────────────────────
const pendingTasks = computed(() => tasks.value.filter(t => !t.is_completed))
const doneTasks    = computed(() => tasks.value.filter(t => t.is_completed))

const todayString = computed(() => {
  return new Date().toLocaleDateString('en-US', { weekday: 'long', month: 'long', day: 'numeric' })
})

// ── Sidebar data ───────────────────────────────────────────────────
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

// ── API calls — this is how your frontend talks to YOUR API ────────

async function fetchTasks() {
  loading.value = true
  error.value   = null
  try {
    const res   = await axios.get(`${API}/tasks`)
    tasks.value = res.data
    apiStatus.value = 'online'
  } catch (e) {
    error.value = `Could not reach API at ${API}/tasks — make sure Docker is running.`
    apiStatus.value = 'offline'
    tasks.value = []
  } finally {
    loading.value = false
  }
}

async function createTask() {
  if (!newTask.value.title) return
  try {
    const res = await axios.post(`${API}/tasks`, {
      title:          newTask.value.title,
      description:    newTask.value.description,
      duration_start: newTask.value.duration_start,
      duration_end:   newTask.value.duration_end,
      is_completed:   false,
    })
    tasks.value.push(res.data)
    newTask.value = { title: '', description: '', duration_start: 900, duration_end: 1000 }
    showForm.value = false
  } catch (e) {
    error.value = 'Failed to create task.'
  }
}

async function deleteTask(id) {
  try {
    await axios.delete(`${API}/tasks/${id}`)
    tasks.value = tasks.value.filter(t => t.id !== id)
  } catch (e) {
    error.value = 'Failed to delete task.'
  }
}

function toggleTask(task) {
  task.is_completed = !task.is_completed
}

// ── Helpers ────────────────────────────────────────────────────────
function formatTime(hhmm) {
  const h = Math.floor(hhmm / 100)
  const m = hhmm % 100
  return `${h}:${m.toString().padStart(2, '0')}`
}

// ── Lifecycle ──────────────────────────────────────────────────────
onMounted(fetchTasks)
</script>

<style scoped>
.app-shell {
  display: flex;
  min-height: 100vh;
}

/* ── SIDEBAR ── */
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

.back-link {
  margin-top: auto;
  font-size: 0.82rem;
  color: var(--text-muted);
  padding: 0.5rem 0.75rem;
  transition: color 0.15s;
}
.back-link:hover { color: var(--text); }

/* ── MAIN ── */
.main {
  flex: 1;
  padding: 2rem 2.5rem;
  overflow-y: auto;
  max-width: 860px;
}
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

/* ── FORM ── */
.task-form {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.5rem;
  margin-bottom: 1.5rem;
}
.form-title { font-size: 1rem; font-weight: 700; margin-bottom: 1rem; }
.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin-bottom: 1rem;
}
.form-full { grid-column: 1 / -1; }
.form-group { display: flex; flex-direction: column; gap: 0.4rem; }
.form-group label { font-size: 0.8rem; color: var(--text-muted); font-weight: 500; }
.form-group input {
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 0.6rem 0.9rem;
  color: var(--text);
  font-size: 0.9rem;
  font-family: inherit;
  transition: border-color 0.15s;
}
.form-group input:focus {
  outline: none;
  border-color: var(--primary);
}
.form-actions { display: flex; justify-content: flex-end; }

/* ── BUTTONS ── */
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
.btn-primary:disabled { opacity: 0.5; cursor: not-allowed; }

/* ── STATS ── */
.stats-bar {
  display: flex;
  gap: 1rem;
  margin-bottom: 1.5rem;
  flex-wrap: wrap;
}
.stat {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 0.75rem 1.25rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  min-width: 80px;
}
.stat-num   { font-size: 1.5rem; font-weight: 800; }
.stat-label { font-size: 0.72rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px; margin-top: 2px; }

/* ── STATE MESSAGES ── */
.state-message {
  text-align: center;
  padding: 3rem;
  color: var(--text-muted);
  font-size: 0.95rem;
}
.state-error {
  color: var(--danger);
  background: rgba(248,113,113,0.1);
  border: 1px solid rgba(248,113,113,0.2);
  border-radius: var(--radius);
}

/* ── TASK LIST ── */
.task-list { display: flex; flex-direction: column; gap: 0.75rem; }

.empty-state {
  text-align: center;
  padding: 4rem;
  color: var(--text-muted);
}
.empty-icon { font-size: 3rem; margin-bottom: 1rem; }

.task-card {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1rem 1.25rem;
  transition: border-color 0.2s, opacity 0.2s;
}
.task-card:hover { border-color: var(--primary); }
.task-card.done  { opacity: 0.5; }

.task-check {
  width: 22px;
  height: 22px;
  min-width: 22px;
  border-radius: 6px;
  border: 2px solid var(--border);
  background: transparent;
  color: var(--success);
  font-size: 0.75rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.15s;
  margin-top: 2px;
}
.task-check:hover { border-color: var(--success); }
.task-card.done .task-check { background: var(--success); border-color: var(--success); color: #fff; }

.task-body { flex: 1; }
.task-title { font-size: 0.95rem; font-weight: 600; }
.task-card.done .task-title { text-decoration: line-through; }
.task-desc  { font-size: 0.82rem; color: var(--text-muted); margin-top: 0.25rem; }
.task-meta  { display: flex; gap: 1rem; margin-top: 0.5rem; font-size: 0.75rem; color: var(--text-muted); }
.task-provider { background: rgba(99,102,241,0.15); color: var(--primary-h); padding: 0.1rem 0.5rem; border-radius: 999px; }

.task-delete {
  border: none;
  background: transparent;
  color: var(--text-muted);
  font-size: 0.8rem;
  padding: 0.25rem;
  border-radius: 4px;
  transition: all 0.15s;
}
.task-delete:hover { color: var(--danger); background: rgba(248,113,113,0.1); }

/* ── TRANSITIONS ── */
.slide-enter-active, .slide-leave-active { transition: all 0.25s ease; }
.slide-enter-from, .slide-leave-to       { opacity: 0; transform: translateY(-10px); }
</style>
