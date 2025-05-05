<template>
  <AdminSideBar />
  <AdminDashboardNavBar />
  <div class="container">
    <div class="row">
      <div class="col-md-2"></div>
      <div class="col-md-10 container">
        <h1>Edit Event</h1>
        <form @submit.prevent="updateEvent" class="contact-form w-100">
          <div class="form-row">
            <div class="form-group col-md-12">
              <label for="title">Event Title:</label>
              <input v-model="event.title" type="text" id="title" class="form-control" />
              <span v-if="errors.title" class="text-danger">{{ errors.title }}</span>
            </div>
            <div class="form-group col-md-12">
              <label for="description">Description:</label>
              <textarea
                v-model="event.description"
                id="description"
                class="form-control"
              ></textarea>
              <span v-if="errors.description" class="text-danger">{{ errors.description }}</span>
            </div>
            <div class="form-group col-md-4">
              <label for="date">Date:</label>
              <input v-model="event.date" type="date" id="date" class="form-control" />
              <span v-if="errors.date" class="text-danger">{{ errors.date }}</span>
            </div>
            <div class="form-group col-md-4">
              <label for="time">Time:</label>
              <input v-model="event.time" type="time" id="time" class="form-control" />
              <span v-if="errors.time" class="text-danger">{{ errors.time }}</span>
            </div>
            <div class="form-group col-md-4">
              <label for="duration">Duration:</label>
              <input v-model="event.duration" type="text" id="duration" class="form-control" />
              <span v-if="errors.duration" class="text-danger">{{ errors.duration }}</span>
            </div>
            <div class="form-group col-md-12">
              <label for="location">Location:</label>
              <input v-model="event.location" type="text" id="location" class="form-control" />
              <span v-if="errors.location" class="text-danger">{{ errors.location }}</span>
            </div>
            <button class="form-control btn btn-primary px-5" type="submit" :disabled="loading">
              {{ loading ? 'Loading...' : 'Update Event' }}
            </button>
            <span v-if="errors.request" class="text-danger">{{ errors.request }}</span>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import AdminSideBar from '@/components/AdminSideBar.vue'
import AdminDashboardNavBar from '@/components/AdminDashboardNavBar.vue'
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '@/services/axios.js'

const event = ref({
  id: '',
  title: '',
  description: '',
  date: '',
  time: '',
  duration: '',
  location: '',
  public: false,
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
const route = useRoute()
const router = useRouter()
const loading = ref(false)

const fetchEvent = async () => {
  const eventId = route.params.id
  try {
    const response = await api.get(`/events/${eventId}`)
    event.value = response.data
  } catch (error) {
    console.error('Error fetching event:', error)
  }
}

const updateEvent = async () => {
  if (!validate()) {
    return
  }

  loading.value = true

  try {
    // 'en-GB' ensures the format DD/MM/YYYY
    event.value.date = new Date(event.value.date).toLocaleDateString('en-GB')
    event.value.time = event.value.time.slice(0, 5)
    const response = await api.put(`/events/${event.value.id}`, event.value, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    })

    if (response.status === 200) {
      alert('Event updated successfully!')
      router.push({ name: 'admin-events' })
    } else {
      errors.value.request = `Failed to update event: ${response.data.error || response.data.message}`
    }
  } catch (error) {
    errors.value.request = `Failed to update event: ${error.response.data.error || error.message}`
    console.error('Error updating event:', error)
  }

  loading.value = false
}

onMounted(() => {
  fetchEvent()
})

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

  if (!event.value.title) {
    errors.value.title = 'Title is required'
  }

  if (!event.value.description) {
    errors.value.description = 'Description is required'
  }

  if (!event.value.date) {
    errors.value.date = 'Date is required'
  }

  if (new Date(event.value.date) < new Date()) {
    errors.value.date = 'Date must be in the future'
  }

  if (!event.value.time) {
    errors.value.time = 'Time is required'
  }

  if (!event.value.duration) {
    errors.value.duration = 'Duration is required'
  }

  if (event.value.duration.length >= 10) {
    errors.value.duration = 'Duration must be less than 10 characters'
  }

  if (!event.value.location) {
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
