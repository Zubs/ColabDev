<template>
  <AdminSideBar />
  <AdminDashboardNavBar />
  <div class="container mt-5">
    <h2>Add New Event</h2>
    <form @submit.prevent="addEvent">
      <div class="form-group">
        <label for="title">Title:</label>
        <input type="text" id="title" v-model="events.title" />
        <span v-if="errors.title" class="text-danger">{{ errors.title }}</span>
      </div>
      <div class="form-group">
        <label for="description">Description:</label>
        <textarea id="description" v-model="events.description"></textarea>
        <span v-if="errors.description" class="text-danger">{{ errors.description }}</span>
      </div>
      <div class="form-group">
        <label for="date">Date:</label>
        <input type="date" id="date" v-model="events.date" />
        <span v-if="errors.date" class="text-danger">{{ errors.date }}</span>
      </div>
      <div class="form-group">
        <label for="time">Time:</label>
        <input type="time" id="time" v-model="events.time" />
        <span v-if="errors.time" class="text-danger">{{ errors.time }}</span>
      </div>
      <div class="form-group">
        <label for="duration">Duration:</label>
        <input type="text" id="duration" v-model="events.duration" />
        <span v-if="errors.duration" class="text-danger">{{ errors.duration }}</span>
      </div>
      <div class="form-group">
        <label for="location">Location:</label>
        <input type="text" id="location" v-model="events.location" />
        <span v-if="errors.location" class="text-danger">{{ errors.location }}</span>
      </div>
      <button type="submit" class="add-event-button" :disabled="loading">
        {{ loading ? 'Loading...' : 'Add Event' }}
      </button>
      <span v-if="errors.request" class="text-danger">{{ errors.request }}</span>
    </form>
  </div>
</template>

<script setup lang="ts">
import AdminSideBar from '@/components/AdminSideBar.vue'
import { ref } from 'vue'
import AdminDashboardNavBar from '@/components/AdminDashboardNavBar.vue'
import api from '@/services/axios.js'
import { useRouter } from 'vue-router'

const events = ref({
  title: '',
  description: '',
  date: '',
  time: '',
  duration: '',
  location: '',
})
const errors = ref({
  title: '',
  description: '',
  date: '',
  time: '',
  duration: '',
  location: '',
  request: '',
})
const router = useRouter()
const loading = ref(false)

const addEvent = async () => {
  if (!validate()) {
    return
  }

  loading.value = true

  try {
    // 'en-GB' ensures the format DD/MM/YYYY
    events.value.date = new Date(events.value.date).toLocaleDateString('en-GB')
    const response = await api.post('/events', {
      ...events.value,
    })

    if (response.status === 201) {
      alert('Event added successfully!')
      await router.push({ name: 'admin-events' })
    } else {
      errors.value.request = `Failed to add event: ${response.data.error || response.data.message}`
    }
  } catch (error) {
    errors.value.request = `Failed to add event: ${error.response.data.error || error.message}`
    console.error('Error:', error)
  }

  loading.value = false
}

const validate = () => {
  errors.value = {
    title: '',
    description: '',
    date: '',
    time: '',
    duration: '',
    location: '',
    request: '',
  }

  if (!events.value.title) {
    errors.value.title = 'Title is required'
  }

  if (!events.value.description) {
    errors.value.description = 'Description is required'
  }

  if (!events.value.date) {
    errors.value.date = 'Date is required'
  }

  if (new Date(events.value.date) < new Date()) {
    errors.value.date = 'Date must be in the future'
  }

  if (!events.value.time) {
    errors.value.time = 'Time is required'
  }

  if (!events.value.duration) {
    errors.value.duration = 'Duration is required'
  }

  if (events.value.duration.length >= 10) {
    errors.value.duration = 'Duration must be less than 10 characters'
  }

  if (!events.value.location) {
    errors.value.location = 'Location is required'
  }

  return (
    !errors.value.date &&
    !errors.value.time &&
    !errors.value.duration &&
    !errors.value.location &&
    !errors.value.title &&
    !errors.value.description
  )
}
</script>

<style scoped>
.container {
  width: 600px;
  height: auto; /* Adjust height to fit content */
  background-color: lightcyan;
  padding: 20px;
  border-radius: 10px;
  position: absolute;
  top: 50%;
  left: 60%;
  transform: translate(-50%, -50%);
  margin-right: 100px;
  margin-top: 120px !important;
}

h2 {
  text-align: center;
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

input[type='text'],
input[type='date'],
input[type='time'],
textarea {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

textarea {
  resize: vertical;
  height: 100px;
}

.add-event-button {
  width: 100%;
  padding: 10px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}

.add-event-button:hover {
  background-color: #45a049;
}
</style>
