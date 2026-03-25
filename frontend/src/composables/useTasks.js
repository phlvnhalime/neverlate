import { ref, computed } from 'vue'
import axios from 'axios'
import { useAuth } from './useAuth'

const API = 'http://localhost:8000'

const tasks     = ref([])
const loading   = ref(true)
const error     = ref(null)
const apiStatus = ref('offline')
const showForm  = ref(false)
const newTask   = ref({ title: '', description: '', duration_start: 900, duration_end: 1000 })

const pendingTasks = computed(() => tasks.value.filter(t => !t.completed))
const doneTasks    = computed(() => tasks.value.filter(t =>  t.completed))

const todayString = computed(() =>
  new Date().toLocaleDateString('en-US', { weekday: 'long', month: 'long', day: 'numeric' })
)

function headers() {
  const { authHeaders } = useAuth()
  return authHeaders()
}

async function fetchTasks() {
  loading.value = true
  error.value   = null
  try {
    const res   = await axios.get(`${API}/tasks`, { headers: headers() })
    tasks.value = res.data
    apiStatus.value = 'online'
  } catch (e) {
    if (e.response?.status === 401) {
      error.value = 'Please log in to see your tasks.'
    } else {
      error.value = `Could not reach API at ${API}/tasks — make sure Docker is running.`
    }
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
      completed:      false,
    }, { headers: headers() })
    tasks.value.push(res.data)
    newTask.value = { title: '', description: '', duration_start: 900, duration_end: 1000 }
    showForm.value = false
  } catch {
    error.value = 'Failed to create task.'
  }
}

async function deleteTask(id) {
  try {
    await axios.delete(`${API}/tasks/${id}`, { headers: headers() })
    tasks.value = tasks.value.filter(t => t.id !== id)
  } catch {
    error.value = 'Failed to delete task.'
  }
}

async function toggleTask(task) {
  const updated = !task.completed
  try {
    await axios.put(`${API}/tasks/${task.id}`, {
      ...task,
      completed: updated,
    }, { headers: headers() })
    task.completed = updated
  } catch {
    error.value = 'Failed to update task.'
  }
}

function formatTime(hhmm) {
  const h = Math.floor(hhmm / 100)
  const m = hhmm % 100
  return `${h}:${m.toString().padStart(2, '0')}`
}

export function useTasks() {
  return {
    tasks, loading, error, apiStatus,
    showForm, newTask,
    pendingTasks, doneTasks, todayString,
    fetchTasks, createTask, deleteTask, toggleTask,
    formatTime,
  }
}
