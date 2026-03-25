<template>
  <div class="app-shell">
    <AppSidebar />
    <main class="main">
      <AppHeader />
      <TaskForm />
      <TaskStats />
      <TaskList />
    </main>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useTasks } from '../composables/useTasks'
import { useAuth } from '../composables/useAuth'
import AppSidebar from '../components/app/AppSidebar.vue'
import AppHeader from '../components/app/AppHeader.vue'
import TaskForm from '../components/app/TaskForm.vue'
import TaskStats from '../components/app/TaskStats.vue'
import TaskList from '../components/app/TaskList.vue'

const { fetchTasks } = useTasks()
const { fetchUser } = useAuth()

onMounted(async () => {
  await fetchUser()
  await fetchTasks()
})
</script>

<style scoped>
.app-shell {
  display: flex;
  min-height: 100vh;
}
.main {
  flex: 1;
  padding: 2rem 2.5rem;
  overflow-y: auto;
  max-width: 860px;
}
</style>
