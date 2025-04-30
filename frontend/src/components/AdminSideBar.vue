<template>
  <div class="container-fluid p-0">
    <div class="d-flex flex-column flex-shrink-0 p-3 bg-light-blue sidebar">
      <router-link :to="{ name: 'admin-dashboard' }" class="text-dark text-decoration-none mb-3 fs-3">Home</router-link>

      <!-- Events dropdown -->
      <div class="dropdown mb-3">
        <div class="d-flex align-items-center justify-content-between w-100">
          <span class="fs-3">Events</span>
          <button class="btn p-0 border-0 bg-transparent arrow-button" @click.stop="toggleEvents">
            <span class="arrow" :class="{ 'arrow-down': isEventsOpen }">▸</span>
          </button>
        </div>

        <div v-show="isEventsOpen" class="dropdown-content ms-4 mt-2">
          <router-link :to="{ name: 'admin-events-create' }"
                       class="dropdown-item text-dark text-decoration-none fs-5 hover-margin">
            Create new events
          </router-link>
          <router-link :to="{ name: 'admin-events' }"
                       class="dropdown-item text-dark text-decoration-none fs-5 hover-margin">
            Existing events
          </router-link>
        </div>
      </div>

      <!-- FAQ dropdown -->
      <div class="dropdown mb-3">
        <div class="d-flex align-items-center justify-content-between w-100">
          <span class="fs-3">FAQ</span>
          <button class="btn p-0 border-0 bg-transparent arrow-button" @click.stop="toggleFAQ">
            <span class="arrow" :class="{ 'arrow-down': isFAQOpen }">▸</span>
          </button>
        </div>

        <div v-show="isFAQOpen" class="dropdown-content ms-4 mt-2">
          <router-link :to="{ name: 'admin-faqs-create' }"
                       class="dropdown-item text-dark text-decoration-none fs-5 hover-margin">
            Add new FAQs
          </router-link>
          <router-link :to="{ name: 'admin-faqs' }"
                       class="dropdown-item text-dark text-decoration-none fs-5 hover-margin">
            Current FAQs
          </router-link>
        </div>
      </div>

      <!-- Staff dropdown -->
      <div class="dropdown mb-3">
        <div class="d-flex align-items-center justify-content-between w-100">
          <span class="fs-3">Staff</span>
          <button class="btn p-0 border-0 bg-transparent arrow-button" @click.stop="toggleStaff">
            <span class="arrow" :class="{ 'arrow-down': isStaffOpen }">▸</span>
          </button>
        </div>

        <div v-show="isStaffOpen" class="dropdown-content ms-4 mt-2">
          <router-link :to="{ name: 'admin-staff-create' }"
                       class="dropdown-item text-dark text-decoration-none fs-5 hover-margin">
            Add new staff
          </router-link>
          <router-link :to="{ name: 'admin-staff' }"
                       class="dropdown-item text-dark text-decoration-none fs-5 hover-margin">
            Manage staff
          </router-link>
        </div>
      </div>

      <!-- Registrations dropdown -->
      <div class="dropdown mb-3">
        <div class="d-flex align-items-center justify-content-between w-100">
          <span class="fs-3">Registrations</span>
          <button class="btn p-0 border-0 bg-transparent arrow-button" @click.stop="toggleRegistrations">
            <span class="arrow" :class="{ 'arrow-down': isRegistrationsOpen }">▸</span>
          </button>
        </div>

        <div v-show="isRegistrationsOpen" class="dropdown-content ms-4 mt-2">
          <router-link :to="{ name: 'admin-registrations' }"
                       class="dropdown-item text-dark text-decoration-none fs-5 hover-margin">
            View registrations
          </router-link>
        </div>
      </div>
    </div>

    <button class="btn btn-outline-dark position-fixed bottom-0 start-50 translate-middle-x mb-3 fs-5 fw-bold logout-button"
            @click="logout">
      LOGOUT
    </button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'

// Separate state for each dropdown
const isEventsOpen = ref(false)
const isFAQOpen = ref(false)
const isStaffOpen = ref(false)
const isRegistrationsOpen = ref(false)
const authStore = useAuthStore()
const router = useRouter()

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
/* Custom light blue background */
.bg-light-blue {
  background-color: lightblue;
}

/* Sidebar fixed positioning and width */
.sidebar {
  width: 300px;
  height: 100vh;
  position: fixed;
  left: 0;
  top: 0;
  z-index: 1000;
}

/* Arrow button styling */
.arrow-button {
  cursor: pointer;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Arrow rotation animation */
.arrow {
  transition: transform 0.3s ease;
  display: inline-block;
  font-size: 1.5rem;
  cursor: pointer;
}

.arrow-down {
  transform: rotate(90deg);
}

/* Dropdown content styling */
.dropdown-content {
  display: flex;
  flex-direction: column;
  gap: 8px;
  font-size: 1.20rem;
}

/* Hover effect for dropdown links */
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
  position: absolute;
  bottom: 20px;
  right: 87%;
  transform: translateX(-50%);
  z-index: 1001;
}

.dropdown > div > span.fs-3 {
  font-size: 1.75rem;
  color: black;
}
.router-link-active, .text-dark {
  font-size: 2rem;
}

</style>
