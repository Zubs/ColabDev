<template>
  <admin-side-bar></admin-side-bar>
  <div class="edit-event-container">
    <div class="form-container">
      <p class="form-title">Edit Event</p>
      <form @submit.prevent="updateEvent">
        <div class="form-group">
          <label for="title">Event Title:</label>
          <input v-model="event.title" type="text" id="title" required />
        </div>

        <div class="form-group">
          <label for="description">Description:</label>
          <textarea v-model="event.description" id="description" required></textarea>
        </div>

        <div class="form-group">
          <label for="date">Date:</label>
          <input v-model="event.date" type="date" id="date" required />
        </div>

        <div class="form-group">
          <label for="time">Time:</label>
          <input v-model="event.time" type="time" id="time" required />
        </div>

        <div class="form-group">
          <label for="duration">Duration:</label>
          <input v-model="event.duration" type="text" id="duration" required />
        </div>

        <div class="form-group">
          <label for="location">Location:</label>
          <input v-model="event.location" type="text" id="location" required />
        </div>
        <button class="submit-button" type="submit">Update Event</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import AdminSideBar from '@/components/AdminSideBar.vue'
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRoute, useRouter } from 'vue-router'

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

const route = useRoute()
const router = useRouter()

const fetchEvent = async () => {
  const eventId = route.params.id
  try {
    const response = await axios.get(`https://opendaywlvapi.onrender.com/events/${eventId}`)
    event.value = response.data
  } catch (error) {
    console.error('Error fetching event:', error)
  }
}

const updateEvent = async () => {
  try {
    const formattedDate = new Date(event.value.date).toLocaleDateString('en-GB'); // 'en-GB' ensures the format DD/MM/YYYY
    event.value.date = formattedDate;
    const response = await axios.put(
      `https://opendaywlvapi.onrender.com/events/${event.value.id}`,
      event.value
    )
    alert(response.data.message)
    router.push('/events')
  } catch (error) {
    console.error('Error updating event:', error)
  }
}

onMounted(() => {
  fetchEvent()
})
</script>

<style scoped>
.edit-event-container {
  width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.form-container {
  background-color: lightcyan;
  padding: 20px;
  border-radius: 8px;
}

.form-title {
  font-size: 32px;
  font-weight: bold;
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  font-size: 16px;
  font-weight: bold;
}

input, textarea {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border-radius: 4px;
  border: 1px solid #ccc;
}

textarea {
  height: 100px;
  resize: none;
}

button.submit-button {
  background-color: #007bff;
  color: white;
  font-size: 16px;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button.submit-button:hover {
  background-color: #0056b3;
}
</style>
