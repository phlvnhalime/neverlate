<template>
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
      <span class="stat-num">{{ completionPercent }}%</span>
      <span class="stat-label">Complete</span>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useTasks } from '../../composables/useTasks'

const { tasks, pendingTasks, doneTasks } = useTasks()

const completionPercent = computed(() =>
  Math.round((doneTasks.value.length / (tasks.value.length || 1)) * 100)
)
</script>

<style scoped>
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
</style>
