<template>
  <div class="task-card" :class="{ done: task.completed }">
    <button class="task-check" @click="$emit('toggle', task)">
      {{ task.completed ? '✓' : '' }}
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
    <button class="task-delete" @click="$emit('delete', task.id)" title="Delete">✕</button>
  </div>
</template>

<script setup>
import { useTasks } from '../../composables/useTasks'

defineProps({ task: Object })
defineEmits(['toggle', 'delete'])

const { formatTime } = useTasks()
</script>

<style scoped>
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
</style>
