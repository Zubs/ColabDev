<template>
  <div>
    <NavBar />
    <div class="background-container">
      <section class="content">
        <!-- Wrapping the heading and paragraph in a div with a background box -->
        <div class="text-box">
          <h1 class="move-rightheader">EVENTS LINED UP</h1>
        </div>
        <p class="move-right">Check out the exciting events taking place during our open days!</p>
      </section>
    </div>

    <!-- Date Selection -->
    <section class="date-selector">
      <button
        v-for="(date, index) in eventDates"
        :key="index"
        @click="selectedDate = date"
        :class="{ active: selectedDate === date }"
      >
        Day {{ index + 1 }} - {{ formatDate(date) }}
      </button>
    </section>

    <!-- Events Section -->
    <section class="events-section">
      <div v-if="loading" class="loading">Loading events...</div>
      <div v-else-if="error" class="error">{{ error }}</div>
      <div v-else-if="filteredEvents.length === 0" class="no-events">
        No events available for this date.
      </div>
      <div v-else class="events-container">
        <div
          v-for="event in filteredEvents"
          :key="event.id || event['Event Title']"
          class="event-card"
        >
          <div class="event-content">
            <h2>📌 {{ event.title }}</h2>
            <p>{{ event.description || 'No description available.' }}</p>
            <p><strong>📅 Date:</strong> {{ formatDate(event.date) }}</p>
            <p><strong>⏰ Time:</strong> {{ event.time || 'TBA' }}</p>
            <p><strong>⏳ Duration:</strong> {{ event.duration || 'TBA' }}</p>
            <p><strong>📍 Location:</strong> {{ event.location || 'TBA' }}</p>
          </div>
        </div>
      </div>
    </section>
    <Footer />
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import api from '@/services/axios.js'
import NavBar from '@/components/NavBar.vue'
import Footer from '@/components/Footer.vue'

// Stating variables
const events = ref<any[]>([])
const loading = ref(true)
const error = ref('')
const selectedDate = ref<string>('')

// Fetch events from API
const fetchEvents = async () => {
  try {
    const response = await api.get('/events')

    // Ensure response
    if (Array.isArray(response.data)) {
      events.value = response.data

      // Set default selected date to the first available date
      if (eventDates.value.length > 0) {
        selectedDate.value = eventDates.value[0]
      }
    } else {
      throw new Error('Invalid API response format')
    }
  } catch (err: any) {
    error.value = err.message || 'Failed to load events. Please try again later.'
  } finally {
    loading.value = false
  }
}

// Extract unique dates from events
const eventDates = computed(() => {
  const uniqueDates = new Set(events.value.map((event) => event.date))
  return Array.from(uniqueDates).sort() // Sort dates in ascending order DO NOT CANGE
})

// Filtering events based on selected date DO NOT CHANGE
const filteredEvents = computed(() => {
  return events.value.filter((event) => event.date === selectedDate.value)
})

// Format date function
const formatDate = (dateString: string | undefined) => {
  if (!dateString) return 'Unknown date'
  const options: Intl.DateTimeFormatOptions = { year: 'numeric', month: 'long', day: 'numeric' }
  return new Date(dateString).toLocaleDateString('en-GB', options)
}

// Fetch events
onMounted(fetchEvents)
</script>

<style scoped>
/* Background container */
.background-container {
  position: relative;
  background-image: url('https://study-net.eu/wp-content/uploads/2020/02/pic_3.jpg');
  background-size: cover;
  background-position: center;
  min-height: 50vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Blur effeect */
.background-container::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: inherit;
  background-size: cover;
  background-position: center;
  filter: blur(5px);
  z-index: -1;
}

/* Content tex styled here */
.content {
  text-align: center;
}

.text-box {
  background-color: lightyellow;
  padding: 15px;
  border-radius: 10px;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
  max-width: 650px;
  margin: 0 auto;
}

.move-right {
  margin-left: 50px;
  font-size: 3.5ch;
  color: white;
}

.move-rightheader {
  margin-left: -21px;
  font-size: 3.5rem;
  font-weight: 900;
  color: black;
}

/* Date selector applied here */
.date-selector {
  display: flex;
  justify-content: center;
  gap: 15px;
  margin: 30px 0;
}

.date-selector button {
  padding: 18px 30px;
  font-size: 1.3rem;
  border: none;
  background-color: #f39c12;
  color: white;
  font-weight: bold;
  cursor: pointer;
  border-radius: 12px;
  transition: all 0.3s ease-in-out;
}

.date-selector button.active {
  background-color: #d35400;
  transform: scale(1.1);
}

.date-selector button:hover {
  background-color: #e67e22;
  transform: scale(1.05);
}

/* Events section */
.events-section {
  padding: 20px;
  text-align: center;
}

/* Ensure events stack vertically or horizantlyy make ameds here  */
.events-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

/* it doesnt work */
.event-card {
  position: relative;
  width: 80%;
  max-width: 600px;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
  transition: transform 0.3s ease-in-out;
  text-align: left;
  background: url('/wlvcourtyard.jpg') center/cover no-repeat;
}

/*it doesnt work */
.event-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: inherit;
  filter: blur(10px);
  z-index: -1;
}

/* Stuff inside the event card */
.event-content {
  position: relative;
  padding: 25px;
  background: rgba(255, 255, 255, 0.85);
  border-radius: 15px;
}

.event-card:hover {
  transform: translateY(-5px);
}

.event-card h2 {
  color: #2c3e50;
  font-size: 1.8rem;
  font-weight: bold;
}

.event-card p {
  color: #7f8c8d;
  font-size: 1.3rem;
  line-height: 1.5;
}
</style>
