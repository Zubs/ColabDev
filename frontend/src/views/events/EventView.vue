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
    <Events />
    <Footer />
  </div>
</template>

<style scoped>
/* Background container with an image */
.background-container {
  position: relative;
  background-image: url('https://study-net.eu/wp-content/uploads/2020/02/pic_3.jpg'); /* Path to your image */
  background-size: cover; /* Ensure the image covers the entire container */
  background-position: center; /* Center the image */
  min-height: 100vh; /* Full height */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 0; /* Layer the content above */
}

/* Apply the blur effect to the background image using a pseudo-element */
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

/* Content area to display text */
.content {
  z-index: 1;
  position: relative;
  text-align: center;
}

@media (min-width: 1024px) {
  .events {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}

/* Styling for the background box */
.text-box {
  background-color: lightyellow;
  padding: 5px; /* Add padding inside the box */
  border-radius: 5px; /* Rounded corners */
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); /* Add a subtle shadow */
  max-width: 600px; /* Limit the width of the box */
  margin: 0 auto; /* Center the box horizontally */
}

.move-right {
  margin-left: 50px;
  font-size: 3ch;
  color: white;
}

.move-rightheader {
  margin-left: -21px; /* Ensure this font is available */
  font-size: 3rem; /* Add size to make the change more noticeable */
  font-weight: 900; /* Change font weight to make it bold */
  color: black;
}
</style>

<script setup lang="ts">
import NavBar from '@/components/NavBar.vue'
import Events from '@/components/Events.vue' // Correctly importing the Events component
import Footer from '@/components/Footer.vue' // Importing the Footer component
</script>
