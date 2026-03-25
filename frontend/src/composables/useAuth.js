import { ref, computed } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const API = 'http://localhost:8000'

const token = ref(localStorage.getItem('token') || null)
const user  = ref(null)
const authError = ref(null)
const authLoading = ref(false)

const isLoggedIn = computed(() => !!token.value)

function setToken(newToken) {
  token.value = newToken
  if (newToken) {
    localStorage.setItem('token', newToken)
  } else {
    localStorage.removeItem('token')
  }
}

function authHeaders() {
  return token.value ? { Authorization: `Bearer ${token.value}` } : {}
}

async function register(data) {
  authLoading.value = true
  authError.value = null
  try {
    await axios.post(`${API}/auth/register`, data)
    return true
  } catch (e) {
    authError.value = e.response?.data?.detail || 'Registration failed'
    return false
  } finally {
    authLoading.value = false
  }
}

async function verifyEmail(email, code) {
  authLoading.value = true
  authError.value = null
  try {
    const res = await axios.post(`${API}/auth/verify`, { email, code })
    setToken(res.data.access_token)
    await fetchUser()
    return true
  } catch (e) {
    authError.value = e.response?.data?.detail || 'Verification failed'
    return false
  } finally {
    authLoading.value = false
  }
}

async function login(email, password) {
  authLoading.value = true
  authError.value = null
  try {
    const res = await axios.post(`${API}/auth/login`, { email, password })
    setToken(res.data.access_token)
    await fetchUser()
    return true
  } catch (e) {
    authError.value = e.response?.data?.detail || 'Login failed'
    return false
  } finally {
    authLoading.value = false
  }
}

async function fetchUser() {
  if (!token.value) return
  try {
    const res = await axios.get(`${API}/auth/me`, { headers: authHeaders() })
    user.value = res.data
  } catch {
    setToken(null)
    user.value = null
  }
}

function logout() {
  setToken(null)
  user.value = null
}

export function useAuth() {
  return {
    token, user, authError, authLoading,
    isLoggedIn, authHeaders,
    register, verifyEmail, login, logout, fetchUser,
  }
}
