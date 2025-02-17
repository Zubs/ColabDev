import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import EventView from '../views/events/EventView.vue'
import HandelEvents from '../views/admin-dashboard/HandelEvents.vue';
import HandelRegistrations from '../views/admin-dashboard/HandelRegistrations.vue';
import HandelVenue from '../views/admin-dashboard/HandelVenue.vue';
import HandelStaff from '../views/admin-dashboard/HandelStaff.vue';
import HandelFAQ from '../views/admin-dashboard/HandelFAQ.vue';
import HandelSecurity from '../views/admin-dashboard/Security.vue';
import DashboardView from '@/views/admin-dashboard/DashboardView.vue'

// Import EventView.vue

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
   },
  {
    path: '/handel-events',
    name: 'handel-events',
    component: HandelEvents,
  },
  {
    path: '/handel-registrations',
    name: 'handel-registrations',
    component: HandelRegistrations,
  },
  {
    path: '/handel-venue',
    name: 'handel-venue',
    component: HandelVenue,
  },
  {
    path: '/handel-staff',
    name: 'handel-staff',
    component: HandelStaff,
  },
  {
    path: '/handel-faq',
    name: 'handel-faq',
    component: HandelFAQ,
  },
  {
    path: '/security',
    name: 'security',
    component: HandelSecurity,
  },
  {
    path: '/admin-dashboard',  // URL path
    name: 'admin-dashboard',  // A name for this route
    component: DashboardView,  // The component to render for this route
  },
];


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
