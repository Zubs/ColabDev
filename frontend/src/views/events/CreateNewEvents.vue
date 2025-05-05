<template>
  <AdminSideBar />
  <AdminDashboardNavBar />
  <div class="container">
    <div class="row">
      <div class="col-md-2"></div>
      <div class="col-md-10 container">
        <h1>Add New Event</h1>
        <form class="contact-form w-100" @submit.prevent="addEvent">
          <div class="form-row">
            <div class="form-group col-md-12">
              <label for="title">Event Title:</label>
              <input
                type="text"
                class="form-control"
                id="title"
                v-model="events.title"
                placeholder="Enter event title"
              />
              <span v-if="errors.title" class="text-danger">{{ errors.title }}</span>
            </div>
            <div class="form-group col-md-12">
              <label for="description">Event Description:</label>
              <textarea
                id="description"
                v-model="events.description"
                class="form-control"
                placeholder="Enter Event Description"
              ></textarea>
              <span v-if="errors.description" class="text-danger">{{ errors.description }}</span>
            </div>
            <div class="form-group col-md-4">
              <label for="date">Event Date:</label>
              <input type="date" id="date" v-model="events.date" class="form-control" />
              <span v-if="errors.date" class="text-danger">{{ errors.date }}</span>
            </div>
            <div class="form-group col-md-4">
              <label for="time">Event Time:</label>
              <input type="time" id="time" v-model="events.time" class="form-control" />
              <span v-if="errors.time" class="text-danger">{{ errors.time }}</span>
            </div>
            <div class="form-group col-md-4">
              <label for="duration">Event Duration:</label>
              <input type="text" id="duration" v-model="events.duration" class="form-control" placeholder="Enter duration like 2hr, 1hr, etc" />
              <span v-if="errors.duration" class="text-danger">{{ errors.duration }}</span>
            </div>
            <div class="form-group col-md-12">
              <label for="location">Event Location:</label>
              <input type="text" id="location" v-model="events.location" class="form-control" placeholder="Enter event location" />
              <span v-if="errors.location" class="text-danger">{{ errors.location }}</span>
            </div>
            <div class="form-group col-md-12 text-center">
              <button type="submit" class="btn btn-primary px-5 form-control" :disabled="loading">
                <span v-if="loading">Processing...</span>
                <span v-else>Add Event</span>
              </button>
              <span v-if="errors.request" class="text-danger">{{ errors.request }}</span>
            </div>
          </div>
        </form>
      </div>
    </div>
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
    const response = await api.post(
      '/events',
      {
        ...events.value,
      },
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
      },
    )

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
