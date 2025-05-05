<template>
  <div class="container-fluid p-0">
    <!-- Hamburger button, only shows when sidebar is closed -->
    <button v-if="!isSidebarOpen" class="hamburger-button" @click="toggleSidebar">
      ☰
    </button>

    <!-- Sidebar only shown when toggled -->
    <div v-if="isSidebarOpen" class="sidebar-wrapper">
      <!-- Main sidebar with scrollable content -->
      <div class="sidebar bg-light-blue">
        <!-- Close button at top-right corner -->
        <div class="d-flex justify-content-end mb-3">
          <button type="button" class="btn-close-custom" aria-label="Close" @click="toggleSidebar">
            <i class="fs-4">×</i>
          </button>
        </div>

        <div class="sidebar-nav">
          <router-link :to="{ name: 'admin-dashboard' }" class="text-dark text-decoration-none mb-3 fs-3">Home</router-link>

          <!-- Events -->
          <div class="dropdown mb-3">
            <div class="d-flex align-items-center justify-content-between w-100">
              <span class="fs-3">Events</span>
              <button class="btn p-0 border-0 bg-transparent arrow-button" @click.stop="toggleEvents">
                <span class="arrow" :class="{ 'arrow-down': isEventsOpen }">▸</span>
              </button>
            </div>
            <div v-show="isEventsOpen" class="dropdown-content ms-4 mt-2">
              <router-link :to="{ name: 'admin-events-create' }" class="dropdown-item text-dark text-decoration-none hover-margin">
                Create new events
              </router-link>
              <router-link :to="{ name: 'admin-events' }" class="dropdown-item text-dark text-decoration-none hover-margin">
                Existing events
              </router-link>
            </div>
          </div>

          <!-- FAQ -->
          <div class="dropdown mb-3">
            <div class="d-flex align-items-center justify-content-between w-100">
              <span class="fs-3">FAQ</span>
              <button class="btn p-0 border-0 bg-transparent arrow-button" @click.stop="toggleFAQ">
                <span class="arrow" :class="{ 'arrow-down': isFAQOpen }">▸</span>
              </button>
            </div>
            <div v-show="isFAQOpen" class="dropdown-content ms-4 mt-2">
              <router-link :to="{ name: 'admin-faqs-create' }" class="dropdown-item text-dark text-decoration-none hover-margin">
                Add new FAQs
              </router-link>
              <router-link :to="{ name: 'admin-faqs' }" class="dropdown-item text-dark text-decoration-none hover-margin">
                Current FAQs
              </router-link>
            </div>
          </div>

          <!-- Staff -->
          <div class="dropdown mb-3">
            <div class="d-flex align-items-center justify-content-between w-100">
              <span class="fs-3">Staff</span>
              <button class="btn p-0 border-0 bg-transparent arrow-button" @click.stop="toggleStaff">
                <span class="arrow" :class="{ 'arrow-down': isStaffOpen }">▸</span>
              </button>
            </div>
            <div v-show="isStaffOpen" class="dropdown-content ms-4 mt-2">
              <router-link :to="{ name: 'admin-staff-create' }" class="dropdown-item text-dark text-decoration-none hover-margin">
                Add new staff
              </router-link>
              <router-link :to="{ name: 'admin-staff' }" class="dropdown-item text-dark text-decoration-none hover-margin">
                Manage staff
              </router-link>
            </div>
          </div>

          <!-- Registrations -->
          <div class="dropdown mb-3">
            <div class="d-flex align-items-center justify-content-between w-100">
              <span class="fs-3">Registrations</span>
              <button class="btn p-0 border-0 bg-transparent arrow-button" @click.stop="toggleRegistrations">
                <span class="arrow" :class="{ 'arrow-down': isRegistrationsOpen }">▸</span>
              </button>
            </div>
            <div v-show="isRegistrationsOpen" class="dropdown-content ms-4 mt-2">
              <router-link :to="{ name: 'admin-registrations' }" class="dropdown-item text-dark text-decoration-none hover-margin">
                View registrations
              </router-link>
            </div>
          </div>
        </div>
      </div>

      <!-- Fixed Logout Button - Separate from scrollable area -->
      <div class="logout-fixed">
        <button class="btn btn-outline-dark logout-button w-100" @click="logout">
          LOGOUT
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'

const isSidebarOpen = ref(false)
const isEventsOpen = ref(false)
const isFAQOpen = ref(false)
const isStaffOpen = ref(false)
const isRegistrationsOpen = ref(false)

const authStore = useAuthStore()
const router = useRouter()

const toggleSidebar = () => {
  isSidebarOpen.value = !isSidebarOpen.value
}

const toggleEvents = () => {
  isEventsOpen.value = !isEventsOpen.value
}
const toggleFAQ = () => {
  isFAQOpen.value = !isFAQOpen.value
}
const toggleStaff = () => {
  isStaffOpen.value = !isStaffOpen.value
}
const toggleRegistrations = () => {
  isRegistrationsOpen.value = !isRegistrationsOpen.value
}

const logout = async () => {
  await authStore.logout()
  await router.push({ name: 'admin-login' })
}
</script>

<style scoped>
.bg-light-blue {
  background-color: lightblue;
}

/* Wrapper to hold both sidebar and fixed logout button */
.sidebar-wrapper {
  position: fixed;
  left: 0;
  top: 0;
  width: 300px;
  height: 100%;
  z-index: 1000;
  display: flex;
  flex-direction: column;
}

.sidebar {
  width: 100%;
  height: calc(100% - 70px); /* Make room for the logout button */
  padding: 15px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.sidebar-nav {
  flex: 1;
  overflow-y: auto;
  padding-right: 5px;
  padding-bottom: 15px;
}

/* Fixed logout button that stays at bottom */
.logout-fixed {
  height: 70px;
  width: 100%;
  background-color: lightblue;
  position: absolute;
  bottom: 0;
  left: 0;
  padding: 15px;
  border-top: 1px solid #ccc;
  z-index: 1001;
  box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
}

.arrow-button {
  cursor: pointer;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.arrow {
  transition: transform 0.3s ease;
  display: inline-block;
  font-size: 1.5rem;
  cursor: pointer;
}

.arrow-down {
  transform: rotate(90deg);
}

.dropdown-content {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.dropdown-content .dropdown-item {
  font-size: 1rem !important; /* Smaller font size for dropdown items */
}

.hover-margin:hover {
  margin-left: 5px !important;
  transition: margin-left 0.2s ease;
}

.logout-button {
  padding: 10px 20px;
  font-size: 1.25rem;
  background-color: #f0f0f0;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.dropdown > div > span.fs-3 {
  font-size: 1.25rem;
  color: black;
}

.router-link-active,
.text-dark {
  font-size: 1.5rem;
}

/* Hamburger button styling */
.hamburger-button {
  position: fixed;
  top: 10px;
  left: 10px;
  z-index: 1100;
  background: transparent;
  border: none;
  font-size: 2rem;
  cursor: pointer;
}

/* Custom close button styling */
.btn-close-custom {
  width: 32px;
  height: 32px;
  background-color: #dc3545;
  color: white;
  border: none;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.2s, transform 0.2s;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

.btn-close-custom:hover {
  background-color: #c82333;
  transform: scale(1.1);
}
</style>
