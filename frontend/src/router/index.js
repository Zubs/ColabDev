import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import EventView from '../views/events/EventView.vue' // Import EventView.vue

const routes = [
  {
    path: '/',
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
    path: '/events',
    name: 'events',
    component: EventView,
  },
  {
      path: '/registration',
      name: 'registration',
      component: () => import('../views/Registration.vue'),
   }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
