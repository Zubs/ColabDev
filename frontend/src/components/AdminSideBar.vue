<template>
  <div class="container">
    <div class="sidebar">
      <router-link :to="{ name: 'admin-dashboard' }" class="sidebar-link">Home</router-link>

      <!-- Events dropdown -->
      <div class="dropdown">
        <button class="dropdown-button" @click="toggleEvents">
          Events
          <span class="arrow" :class="{ 'arrow-down': isEventsOpen }">▸</span>
        </button>

        <div class="dropdown-content" v-show="isEventsOpen">
          <router-link :to="{ name: 'admin-events-create' }" class="dropdown-link"
            >Create new events
          </router-link>
          <router-link :to="{ name: 'admin-events' }" class="dropdown-link"
            >Existing events
          </router-link>
        </div>
      </div>

      <!-- Venue dropdown -->
      <div class="dropdown">
        <button class="dropdown-button" @click="toggleVenue">
          Venue
          <span class="arrow" :class="{ 'arrow-down': isVenueOpen }">▸</span>
        </button>

        <div class="dropdown-content" v-show="isVenueOpen">
          <a href="#" class="dropdown-link">Create new venue</a>
          <a href="#" class="dropdown-link">Existing venues</a>
        </div>
      </div>

      <!-- FAQ dropdown -->
      <div class="dropdown">
        <button class="dropdown-button" @click="toggleFAQ">
          FAQ
          <span class="arrow" :class="{ 'arrow-down': isFAQOpen }">▸</span>
        </button>

        <div class="dropdown-content" v-show="isFAQOpen">
          <a href="#" class="dropdown-link">Add new FAQs</a>
          <a href="#" class="dropdown-link">Current FAQs</a>
        </div>
      </div>

      <!-- Staff dropdown -->
      <div class="dropdown">
        <button class="dropdown-button" @click="toggleStaff">
          Staff
          <span class="arrow" :class="{ 'arrow-down': isStaffOpen }">▸</span>
        </button>

        <div class="dropdown-content" v-show="isStaffOpen">
          <router-link :to="{ name: 'admin-staff-create' }" class="dropdown-link"
            >Add new staff
          </router-link>
          <router-link :to="{ name: 'admin-staff' }" class="dropdown-link"
            >Manage staff
          </router-link>
        </div>
      </div>

      <!-- Registrations dropdown -->
      <div class="dropdown">
        <button class="dropdown-button" @click="toggleRegistrations">
          Registrations
          <span class="arrow" :class="{ 'arrow-down': isRegistrationsOpen }">▸</span>
        </button>

        <div class="dropdown-content" v-show="isRegistrationsOpen">
          <router-link :to="{ name: 'admin-registrations' }" class="dropdown-link"
            >View registrations
          </router-link>
        </div>
      </div>
    </div>
  </div>

  <button class="logout-button" @click="logout">LOGOUT</button>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'

// Separate state for each dropdown
const isEventsOpen = ref(false)
const isVenueOpen = ref(false)
const isFAQOpen = ref(false)
const isStaffOpen = ref(false)
const isRegistrationsOpen = ref(false)
const authStore = useAuthStore()
const router = useRouter()

const toggleEvents = () => {
  isEventsOpen.value = !isEventsOpen.value
}

const toggleVenue = () => {
  isVenueOpen.value = !isVenueOpen.value
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

<style>
/* Reset default margins and padding */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  margin: 0;
  padding: 0;
}
</style>

<style scoped>
.sidebar {
  display: flex;
  flex-direction: column;
  padding: 20px;
  background-color: lightblue;
  width: 300px;
  height: 100%;
  position: fixed;
  left: 0;
  top: 0;
  bottom: 0;
}

.sidebar-link {
  color: black;
  text-decoration: none;
  margin-bottom: 10px;
  font-size: 30px;
}

.container {
  display: flex;
}

/* Dropdown styles */
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
  position: fixed; /* Keep it visible even when scrolling */
  bottom: 20px; /* Position at the bottom */
  left: 50%; /* Center it horizontally */
  transform: translateX(-590%); /* Adjust to be exactly centered */
  background-color: white;
  border: 2px solid black;
  padding: 10px 20px;
  cursor: pointer;
}
</style>
