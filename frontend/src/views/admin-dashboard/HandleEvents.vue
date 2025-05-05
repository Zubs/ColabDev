<template>
  <AdminSideBar />
  <AdminDashboardNavBar />
  <div class="container">
    <div class="row">
      <div class="col-md-2"></div>
      <div class="col-md-10 container">
        <h1>
          Events: {{ events.length }}
          <button class="btn btn-primary float-right" @click="goToCreatePage">Add New Event</button>
        </h1>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">ID</th>
              <th scope="col">Event</th>
              <th scope="col">Time</th>
              <th scope="col">Date</th>
              <th scope="col"></th>
              <th scope="col"></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(event, index) in events" :key="index">
              <th scope="row">{{ event.id }}</th>
              <td>{{ event.title }}</td>
              <td>{{ event.time }}</td>
              <td>{{ new Date(event.date).toDateString() }}</td>
              <td>
                <router-link
                  :to="{ name: 'admin-events-edit', params: { id: event.id } }"
                  class="btn btn-warning"
                  >Edit
                </router-link>
              </td>
              <td>
                <button @click="deleteEvent(event.id)" class="btn btn-danger">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import AdminSideBar from '@/components/AdminSideBar.vue'
import { onMounted, ref } from 'vue'
import api from '@/services/axios.js'
import AdminDashboardNavBar from '@/components/AdminDashboardNavBar.vue'
import { useRouter } from 'vue-router'

const events = ref([])
const router = useRouter()

// Fetch all events
const fetchEvents = async () => {
  try {
    const response = await api.get(`/events`)
    events.value = response.data
  } catch (error) {
    console.error('Error fetching Events:', error)
    alert('Failed to fetch events. Please try again later.')
  }
}

// Delete an event
const deleteEvent = async (eventId) => {
  if (!confirm('Are you sure you want to delete this event?')) {
    return // Exit if the user cancels
  }

  try {
    const response = await api.delete(`/events/${eventId}`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    })

    if (response.status === 200) {
      alert('Event deleted successfully')
      events.value = events.value.filter((event) => event?.id !== eventId)
    }
  } catch (error) {
    console.error('Error deleting event:', error)
    alert('Failed to delete event')
  }
}

const goToCreatePage = () => {
  router.push({ name: 'admin-events-create' })
}

// Fetch events when the component is mounted
onMounted(() => {
  fetchEvents()
})
</script>
