import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('../views/HomeView.vue'),
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
        component: () => import('../views/admin-dashboard/DashboardView.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: 'registrations',
        name: 'admin-registrations',
        component: () => import('../views/admin-dashboard/HandleRegistrations.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: 'staff',
        name: 'admin-staff',
        component: () => import('../views/admin-dashboard/HandleStaff.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: 'staff/create',
        name: 'admin-staff-create',
        component: () => import('../views/admin-dashboard/CreateStaff.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: 'events',
        name: 'admin-events',
        component: () => import('../views/admin-dashboard/HandleEvents.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: 'events/create',
        name: 'admin-events-create',
        component: () => import('../views/events/CreateNewEvents.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: 'events/:id/edit',
        name: 'admin-events-edit',
        component: () => import('../views/events/EditEvents.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: 'faqs',
        name: 'admin-faqs',
        component: () => import('../views/admin-dashboard/HandleFAQ.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: 'faqs/create',
        name: 'admin-faqs-create',
        component: () => import('../views/admin-dashboard/CreateFAQ.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: 'faqs/:id/edit',
        name: 'admin-faqs-edit',
        component: () => import('../views/admin-dashboard/EditFAQ.vue'),
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
    component: () => import('../views/events/EventView.vue'),
  },
  {
    path: '/registration',
    name: 'registration',
    component: () => import('../views/RegistrationView.vue'),
  },
  {
    path: '/faqs',
    name: 'faqs',
    component: () => import('../views/faq/FAQView.vue'),
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
