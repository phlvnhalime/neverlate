<template>
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
</template>

<script setup>
import { useTasks } from '../../composables/useTasks'

const { showForm, newTask, createTask } = useTasks()
</script>

<style scoped>
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

.slide-enter-active, .slide-leave-active { transition: all 0.25s ease; }
.slide-enter-from, .slide-leave-to       { opacity: 0; transform: translateY(-10px); }
</style>
