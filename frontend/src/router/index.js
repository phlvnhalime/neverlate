import { createRouter, createWebHistory } from 'vue-router'
import { isTauri } from '../utils/platform'
import LandingView from '../views/LandingView.vue'
import AppView from '../views/AppView.vue'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import VerifyEmailView from '../views/VerifyEmailView.vue'

const routes = [
  {
    path: '/',
    name: 'landing',
    component: LandingView,
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: AppView,
    meta: { requiresAuth: true, appOnly: true },
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView,
  },
  {
    path: '/verify',
    name: 'verify',
    component: VerifyEmailView,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const isApp = isTauri()
  const hasToken = !!localStorage.getItem('token')

  if (to.path === '/' && isApp) {
    next(hasToken ? { name: 'dashboard' } : { name: 'login' })
  } else if (to.meta.appOnly && !isApp) {
    next({ name: 'landing' })
  } else if (to.meta.requiresAuth && !hasToken) {
    next({ name: 'login' })
  } else if ((to.name === 'signup' || to.name === 'verify') && isApp) {
    next({ name: 'login' })
  } else {
    next()
  }
})

export default router
