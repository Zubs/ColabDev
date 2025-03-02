<template>
  <admin-side-bar></admin-side-bar>
  <div class="box-container">
    <div class="button-container">
      <router-link to="/create-new-events" class="add-button">Create New Event</router-link>
    </div>
    <div class="box">
      <p class="text">Active events:</p>
      <table class="table">
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
              <button class="btn btn-warning">Edit</button>
            </td>
            <td>
              <button class="btn btn-danger">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import AdminSideBar from '@/components/AdminSideBar.vue'
import { onMounted, ref } from 'vue'
import axios from 'axios'
import CreateNewEvents from '@/views/events/CreateNewEvents.vue'

const events = ref([])

const fetchEvents = async () => {
  try {
    const response = await axios.get(`https://opendaywlvapi.onrender.com/events`)
    events.value = response.data
  } catch (error) {
    console.error('Error fetching Events:', error)
  }
}

onMounted(() => {
  fetchEvents()
})
</script>

<style scoped>
.box-container {
  position: relative;
  width: 850px;
  margin: 0 auto;
  margin-bottom: 60px;
  bottom: -70px;
  margin-left: 493px;
}

.button-container {
  position: absolute;
  top: -60px;
  right: 0;
  z-index: 1;
}

.add-button {
  padding: 10px 30px;
  font-size: 16px;
  cursor: pointer;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
}

.add-button:hover {
  background-color: #0056b3;
}

.box {
  width: 850px;
  height: 500px;
  background-color: lightcyan;
  padding-left: 20px;
  text-align: left;
  position: relative;
  margin-top: 60px;
  margin-bottom: 60px;
}

.text {
  font-size: 45px;
  color: black;
}

.table {
  font-size: 20px;
  color: black;
}
</style>
