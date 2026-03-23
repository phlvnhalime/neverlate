import { createRouter, createWebHistory } from 'vue-router'
import LandingView from '../views/LandingView.vue'
import AppView from '../views/AppView.vue'

const routes = [
  {
    path: '/',
    name: 'landing',
    component: LandingView,
  },
]

export default createRouter({
  history: createWebHistory(),
  routes,
})
