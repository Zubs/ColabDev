import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import EventView from '../views/events/EventView.vue' // Import EventView.vue

const routes = [
  {
    path: '/home',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/admin',
    name: 'admin',
    children: [
      {
        name: 'admin-login',
        path: 'login',
        component: () => import('../views/admin/LoginView.vue'),
      }
    ],
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('../views/AboutView.vue'),
  },
  {
    path: '/events', // Add the EventView route
    name: 'events',
    component: EventView,
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
