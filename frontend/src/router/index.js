import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import EventView from '../views/events/EventView.vue'
import HandleEvents from '../views/admin-dashboard/HandleEvents.vue'
import HandleRegistrations from '../views/admin-dashboard/HandleRegistrations.vue'
import HandleVenue from '../views/admin-dashboard/HandleVenue.vue'
import HandleStaff from '../views/admin-dashboard/HandleStaff.vue'
import HandleFAQ from '../views/admin-dashboard/HandleFAQ.vue'
import HandleSecurity from '../views/admin-dashboard/Security.vue'
import DashboardView from '@/views/admin-dashboard/DashboardView.vue'
import FAQView from '../views/faq/faq.vue'
import { useAuthStore } from '@/stores/auth'

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
      },
      {
        path: '',
        name: 'admin-dashboard',
        component: DashboardView,
        meta: { requiresAuth: true },
      },
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
  },
  {
    path: '/handle-events',
    name: 'handle-events',
    component: HandleEvents,
  },
  {
    path: '/handle-registrations',
    name: 'handle-registrations',
    component: HandleRegistrations,
  },
  {
    path: '/handle-venue',
    name: 'handle-venue',
    component: HandleVenue,
  },
  {
    path: '/handle-staff',
    name: 'handle-staff',
    component: HandleStaff,
  },
  {
    path: '/handle-faq',
    name: 'handle-faq',
    component: HandleFAQ,
  },
  {
    path: '/security',
    name: 'security',
    component: HandleSecurity,
  },
  {
    path: '/faqs',
    name: 'faqs',
    component: FAQView,
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()

  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next({ name: 'admin-login' }) // Redirect to log in if not authenticated
  } else {
    next() // Allow access
  }
})

export default router
