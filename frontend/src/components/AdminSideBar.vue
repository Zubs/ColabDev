<script setup>
import { ref } from 'vue'

const isHelpOpen = ref(false)

const toggleHelp = () => {
  isHelpOpen.value = !isHelpOpen.value
}
</script>

<template>
  <div class="container">
    <div class="sidebar">
      <a href="#" class="sidebar-link">My profile</a>

      <!-- Help dropdown section -->
      <div class="dropdown">
        <button class="dropdown-button" @click="toggleHelp">
          Help
          <span class="arrow" :class="{ 'arrow-down': isHelpOpen }">▸</span>
        </button>

        <div class="dropdown-content" v-show="isHelpOpen">
          <a href="#" class="dropdown-link">Contact Support</a>
          <a href="#" class="dropdown-link">User Guide</a>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
/* Reset default margins and padding */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  margin: 0;
  padding: 0;
}
</style>

<style scoped>
.sidebar {
  display: flex;
  flex-direction: column;
  padding: 20px;
  background-color: lightblue;
  width: 300px;
  height: 100%;
  position: fixed;
  left: 0;
  top: 0;
  bottom: 0;
}

.sidebar-link {
  color: black;
  text-decoration: none;
  margin-bottom: 10px;
  font-size: 30px;
}

.container {
  display: flex;
}

/* Dropdown styles */
.dropdown {
  margin-top: 10px;
}

.dropdown-button {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  padding: 0;
  font-size: 30px;
  background: none;
  border: none;
  cursor: pointer;
  color: black;
  text-align: left;
}

.arrow {
  transition: transform 0.3s ease;
  display: inline-block;
}

.arrow-down {
  transform: rotate(90deg);
}

.dropdown-content {
  margin-left: 20px;
  margin-top: 10px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.dropdown-link {
  color: black;
  text-decoration: none;
  font-size: 20px;
  transition: margin-left 0.3s ease;
}

.dropdown-link:hover {
  margin-left: 5px;
}
</style>
