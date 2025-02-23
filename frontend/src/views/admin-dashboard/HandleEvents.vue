<template>
  <admin-side-bar></admin-side-bar>
  <div class="box-container">
    <div class="button-container">
      <button class="add-button" @click="addNewEvent">Add New Event</button>
    </div>
    <div class="box">
      <p class="text"> Active events: </p>
      <ul class="text-list">
        <li v-for="(event, index) in events" :key="index">
          <div class="event-header" @click="toggleDropdown(index)">
            {{ event.name }}
            <span class="arrow">{{ openIndex === index ? "▲" : "▼" }}</span>
          </div>
          <div v-show="openIndex === index" class="dropdown-content">
            {{ event.details }}
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import AdminSideBar from '@/components/adminSideBar.vue'

export default {
  components: { AdminSideBar },
  data() {
    return {
      events: [
        { name: "EVENT 1", details: "Details about Event 1" },
        { name: "EVENT 2", details: "Details about Event 2" },
        { name: "EVENT 3", details: "Details about Event 3" }
      ],
      openIndex: null // Keeps track of which dropdown is open
    };
  },
  methods: {
    toggleDropdown(index) {
      this.openIndex = this.openIndex === index ? null : index;
    },
    addNewEvent() {
      // Add your logic to add a new event here
      console.log("Add New Event clicked");
    }
  }
};
</script>

<style scoped>
.box-container {
  position: relative;
  width: 850px;
  margin: 0 auto;
  margin-bottom: 60px;
  bottom: -70px;
  margin-left:493px;
}

.button-container {
  position: absolute;
  top: -60px; /* Move the button above the box */
  right: 0; /* Align the button to the right */
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
  margin-top: 60px; /* Add space for the button */
  margin-bottom: 60px;
}

.text {
  font-size: 45px;
  color: black;
}

.text-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.text-list li {
  margin-bottom: 10px;
  font-size: 25px;
  cursor: pointer;
}

.event-header {
  font-weight: bold;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.arrow {
  font-size: 20px;
  margin-left: 10px;
}

.dropdown-content {
  padding: 5px;
  font-size: 20px;
  background-color: white;
  border: 1px solid #ccc;
  margin-top: 5px;
}
</style>
