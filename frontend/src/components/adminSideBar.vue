<template>
  <div :class="['sidebar', { 'sidebar--collapsed': isCollapsed }]">
    <!-- Toggle button (visible on mobile) -->
    <button class="toggle-button" @click="isCollapsed = !isCollapsed">☰</button>

    <!-- Sidebar content -->
    <div class="sidebar-content">
      <router-link :to="{ name: 'admin-dashboard' }" class="sidebar-link">Home</router-link>

      <!-- Events dropdown -->
      <div class="dropdown">
        <button class="dropdown-button" @click="toggleEvents">
          Events
          <span class="arrow" :class="{ 'arrow-down': isEventsOpen }">▸</span>
        </button>
        <div class="dropdown-content" v-show="isEventsOpen">
          <router-link :to="{ name: 'admin-events-create' }" class="dropdown-link">Create new events</router-link>
          <router-link :to="{ name: 'admin-events' }" class="dropdown-link">Existing events</router-link>
        </div>
      </div>

      <!-- FAQ dropdown -->
      <div class="dropdown">
        <button class="dropdown-button" @click="toggleFAQ">
          FAQ
          <span class="arrow" :class="{ 'arrow-down': isFAQOpen }">▸</span>
        </button>
        <div class="dropdown-content" v-show="isFAQOpen">
          <router-link :to="{ name: 'admin-faqs-create' }" class="dropdown-link">Add new FAQs</router-link>
          <router-link :to="{ name: 'admin-faqs' }" class="dropdown-link">Current FAQs</router-link>
        </div>
      </div>

      <!-- Staff dropdown -->
      <div class="dropdown">
        <button class="dropdown-button" @click="toggleStaff">
          Staff
          <span class="arrow" :class="{ 'arrow-down': isStaffOpen }">▸</span>
        </button>
        <div class="dropdown-content" v-show="isStaffOpen">
          <router-link :to="{ name: 'admin-staff-create' }" class="dropdown-link">Add new staff</router-link>
          <router-link :to="{ name: 'admin-staff' }" class="dropdown-link">Manage staff</router-link>
        </div>
      </div>

      <!-- Registrations dropdown -->
      <div class="dropdown">
        <button class="dropdown-button" @click="toggleRegistrations">
          Registrations
          <span class="arrow" :class="{ 'arrow-down': isRegistrationsOpen }">▸</span>
        </button>
        <div class="dropdown-content" v-show="isRegistrationsOpen">
          <router-link :to="{ name: 'admin-registrations' }" class="dropdown-link">View registrations</router-link>
        </div>
      </div>

      <!-- Logout -->
      <button class="logout-button" @click="logout">LOGOUT</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'

const isCollapsed = ref(window.innerWidth < 768)

const isEventsOpen = ref(false)
const isFAQOpen = ref(false)
const isStaffOpen = ref(false)
const isRegistrationsOpen = ref(false)

const authStore = useAuthStore()
const router = useRouter()

const toggleEvents = () => (isEventsOpen.value = !isEventsOpen.value)
const toggleFAQ = () => (isFAQOpen.value = !isFAQOpen.value)
const toggleStaff = () => (isStaffOpen.value = !isStaffOpen.value)
const toggleRegistrations = () => (isRegistrationsOpen.value = !isRegistrationsOpen.value)

const logout = async () => {
  await authStore.logout()
  await router.push({ name: 'admin-login' })
}

// Auto-collapse sidebar on small screens when resized
window.addEventListener('resize', () => {
  isCollapsed.value = window.innerWidth < 768
})
</script>

<style scoped>
.sidebar {
  background-color: lightblue;
  width: 300px;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 100;
  padding: 20px;
  transition: transform 0.3s ease;
}

/* When collapsed, slide it off-screen */
.sidebar--collapsed {
  transform: translateX(-100%);
}

/* ☰ button for toggling */
.toggle-button {
  display: none;
  position: absolute;
  top: 10px;
  left: 10px;
  font-size: 30px;
  background: white;
  border: 1px solid black;
  padding: 5px 10px;
  z-index: 200;
  cursor: pointer;
}

/* Show toggle button only on small screens */
@media (max-width: 768px) {
  .toggle-button {
    display: block;
  }
}

.sidebar-link {
  color: black;
  text-decoration: none;
  margin-bottom: 10px;
  font-size: 30px;
}

.dropdown {
  margin-top: 10px;
}

.dropdown-button {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  padding: 0;
  font-size: 30px;
  background: none;
  border: none;
  cursor: pointer;
  color: black;
  text-align: left;
}

.arrow {
  transition: transform 0.3s ease;
  display: inline-block;
}

.arrow-down {
  transform: rotate(90deg);
}

.dropdown-content {
  margin-left: 20px;
  margin-top: 10px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.dropdown-link {
  color: black;
  text-decoration: none;
  font-size: 20px;
  transition: margin-left 0.3s ease;
}

.dropdown-link:hover {
  margin-left: 5px;
}

.logout-button {
  font-size: 20px;
  font-weight: bold;
  color: black;
  background-color: white;
  border: 2px solid black;
  padding: 10px 20px;
  cursor: pointer;
  margin-top: auto;
}
</style>
