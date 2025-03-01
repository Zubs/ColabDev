<template>
  <admin-side-bar></admin-side-bar>
  <div class="container">
    <h2>Add New Event</h2>
    <form @submit.prevent="addEvent">
      <div class="form-group">
        <label for="title">Title:</label>
        <input type="text" id="title" v-model="events.title" required />
      </div>
      <div class="form-group">
        <label for="description">Description:</label>
        <textarea id="description" v-model="events.description" required ></textarea>
      </div>
      <div class="form-group">
        <label for="date">Date:</label>
        <input type="date" id="date" v-model="events.date" required />
      </div>
      <div class="form-group">
        <label for="time">Time:</label>
        <input type="time" id="time" v-model="events.time" required />
      </div>
      <div class="form-group">
        <label for="duration">Duration:</label>
        <input type="text" id="duration" v-model="events.duration" required />
      </div>
      <div class="form-group">
        <label for="location">Location:</label>
        <input type="text" id="location" v-model="events.location" required />
      </div>
      <button type="submit" class="add-event-button">Add Event</button>
    </form>
  </div>
</template>

<script setup lang="ts">
import AdminSideBar from '@/components/AdminSideBar.vue';
import { ref } from 'vue'
const events = ref({
  title: '',
  description: '',
  date: '',
  time: '',
  duration: '',
  location: '',
})

const addEvent = async () => {
  try {
    const response = await fetch('https://opendaywlvapi.onrender.com/events', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(events.value),
    });

    if (response.ok) {
      alert('Event added successfully!');
      events.value = {
        title: '',
        description: '',
        date: '',
        time: '',
        duration: '',
        location: '',
      };
    } else {
      const errorData = await response.json();
      alert(`Failed to add event: ${errorData.error || 'Unknown error'}`);
    }
  } catch (error) {
    alert('Network error. Please try again.');
    console.error('Error:', error);
  }
};

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

input[type="text"],
input[type="date"],
input[type="time"],
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
  background-color: #4CAF50;
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
