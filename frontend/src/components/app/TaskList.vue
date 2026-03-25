<template>
  <div v-if="loading" class="state-message">⏳ Loading tasks from API...</div>
  <div v-else-if="error" class="state-message state-error">⚠️ {{ error }}</div>

  <div v-else class="task-list">
    <div v-if="tasks.length === 0" class="empty-state">
      <div class="empty-icon">✅</div>
      <p>No tasks yet. Add your first one above!</p>
    </div>

    <TaskCard
      v-for="task in tasks"
      :key="task.id"
      :task="task"
      @toggle="toggleTask"
      @delete="deleteTask"
    />
  </div>
</template>

<script setup>
import { useTasks } from '../../composables/useTasks'
import TaskCard from './TaskCard.vue'

const { tasks, loading, error, toggleTask, deleteTask } = useTasks()
</script>

<style scoped>
.task-list { display: flex; flex-direction: column; gap: 0.75rem; }

.empty-state {
  text-align: center;
  padding: 4rem;
  color: var(--text-muted);
}
.empty-icon { font-size: 3rem; margin-bottom: 1rem; }

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
</style>
