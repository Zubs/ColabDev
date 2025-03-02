<template>
  <div>
    <h2>Edit Event</h2>
    <form @submit.prevent="updateEvent">
      <label>Title:</label>
      <input v-model="event.title" type="text" />

      <label>Description:</label>
      <textarea v-model="event.description"></textarea>

      <label>Location:</label>
      <input v-model="event.location" type="text" />

      <label>Duration:</label>
      <input v-model="event.duration" type="text" />

      <label>Time:</label>
      <input v-model="event.time" type="time" />

      <label>Date:</label>
      <input v-model="event.date" type="date" />

      <button type="submit">Update Event</button>
    </form>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRoute, useRouter } from 'vue-router';

export default {
  name: 'EditEvent',
  setup() {
    const route = useRoute(); // Get route params (event ID)
    const router = useRouter();

    const event = ref({
      title: '',
      description: '',
      location: '',
      duration: '',
      time: '',
      date: ''
    });

    const fetchEventDetails = async () => {
      try {
        const response = await axios.get(`https://opendaywlvapi.onrender.com/events/${route.params.id}`);
        event.value = response.data;
      } catch (error) {
        console.error('Error fetching event details:', error);
      }
    };

    const updateEvent = async () => {
      try {
        const response = await axios.put(
          `https://opendaywlvapi.onrender.com/events/${route.params.id}`,
          event.value
        );
        console.log('Event updated successfully:', response.data);
        router.push('/'); // Navigate back to the events list after successful update
      } catch (error) {
        console.error('Error updating event:', error);
      }
    };

    onMounted(() => {
      fetchEventDetails();
    });

    return {
      event,
      updateEvent
    };
  }
};
</script>

<style scoped>
/* You can keep your previous styles here */
</style>
