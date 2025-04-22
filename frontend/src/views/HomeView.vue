<template>
  <div>
    <NavBar :solid-background="true" />

    <!-- MAIN Section -->
    <section class="hero-wrapper">
      <div class="hero-content">
        <h1>University of Wolverhampton Open Day</h1>
        <h2 class="hero-subheading">5 July 2025</h2>
        <div class="countdown-wrapper">
          <div class="countdown-item">
            <span class="countdown-number">{{ days }}</span>
            <span class="countdown-label">Days</span>
          </div>
          <div class="countdown-item">
            <span class="countdown-number">{{ hours }}</span>
            <span class="countdown-label">Hours</span>
          </div>
          <div class="countdown-item">
            <span class="countdown-number">{{ minutes }}</span>
            <span class="countdown-label">Minutes</span>
          </div>
          <div class="countdown-item">
            <span class="countdown-number">{{ seconds }}</span>
            <span class="countdown-label">Seconds</span>
          </div>
        </div>
        <div class="button-wrapper" style="margin-top: 30px;">
          <RouterLink :to="{ name: 'registration' }" class="section-button">
  Book Now
</RouterLink>


        </div>
      </div>
    </section>

    <!--  Open Day Video Sction blocK -->
    <section class="section-wrapper">
      <div class="section-card wide-card">
        <h2 class="section-heading">Prepare for undergraduate open day...</h2>
        <p class="section-description">
          Our undergraduate open day is ideal for every prospective student. Whether you just want to get an idea of what the University is like, or want to find out more about a specific subject or course, it's the perfect chance to discover what it's like to study with us.
        </p>
        <div class="video-container">
          <iframe
            src="https://www.youtube.com/embed/CuOINQvswsA?start=1&rel=0"
            title="Explore The University Of Wolverhampton"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            allowfullscreen
          ></iframe>
        </div>
      </div>
    </section>

    <!-- Open Day Guide Section -->
    <section class="section-wrapper">
      <div class="section-card">
        <h2 class="section-heading">Open Day Guide</h2>
        <p class="section-description">
          This is your go-to resource for everything you need on your visit.
        </p>
        <div class="button-wrapper">
          <a
            href="https://www.wlv.ac.uk/news-and-events/open-day/open-day-guide/?utm_medium=cpc&utm_source=google&utm_campaign=ug2025_ucasextra"
            target="_blank"
            class="section-button"
          >
            Click Here
          </a>
        </div>
      </div>
    </section>

    <!-- Our Campuses Section -->
    <section class="campuses-section">
      <h2 class="section-heading">Our Campuses</h2>
      <div class="campuses-container">
        <div
          v-for="(campus, index) in campuses"
          :key="index"
          class="campus-card"
        >
          <div class="campus-content">
            <img :src="campus.image" alt="Campus Image" class="campus-img" />
            <h2>{{ campus.name }}</h2>
            <p>{{ campus.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Open Day Location Map Section -->
    <section class="section-wrapper">
      <div class="section-card wide-card">
        <h2 class="section-heading">Open Day Location</h2>
        <div class="map-container">
          <iframe
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2423.9801138425396!2d-2.1300580232857773!3d52.58805277207909!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x487083cb0f37dc97%3A0x9cb8e3cc0509a0d0!2sUniversity%20of%20Wolverhampton!5e0!3m2!1sen!2suk!4v1745280216079!5m2!1sen!2suk"
            width="100%"
            height="450"
            style="border:0;"
            allowfullscreen=""
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade"
          ></iframe>
        </div>
        <div class="button-wrapper">
          <a
            href="https://www.google.com/maps/place/University+of+Wolverhampton/@52.5880528,-2.130058,17z/"
            target="_blank"
            class="section-button"
          >
            View Larger Map
          </a>
        </div>
      </div>
    </section>

    <Footer />
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import NavBar from '@/components/NavBar.vue'
import Footer from '@/components/Footer.vue'

import cityImage from '@/assets/city.jpg'
import telfordImage from '@/assets/telford.jpg'
import walsallImage from '@/assets/walsall.jpg'
import springfieldImage from '@/assets/springfield.jpg'

const campuses = ref([
  { name: 'City Campus', description: 'The central hub for innovation and leadership.', image: cityImage },
  { name: 'Telford Campus', description: 'Home to our arts and culture departments.', image: telfordImage },
  { name: 'Walsall Campus', description: 'Focuses on business and entrepreneurship.', image: walsallImage },
  { name: 'Springfield Campus', description: 'Specialized in research and development.', image: springfieldImage },
])

const days = ref(0)
const hours = ref(0)
const minutes = ref(0)
const seconds = ref(0)
let timer

const targetDate = new Date('2025-07-05T00:00:00')

const updateCountdown = () => {
  const now = new Date()
  const diff = targetDate - now

  if (diff <= 0) {
    days.value = hours.value = minutes.value = seconds.value = 0
    clearInterval(timer)
    return
  }

  days.value = Math.floor(diff / (1000 * 60 * 60 * 24))
  hours.value = Math.floor((diff / (1000 * 60 * 60)) % 24)
  minutes.value = Math.floor((diff / (1000 * 60)) % 60)
  seconds.value = Math.floor((diff / 1000) % 60)
}

onMounted(() => {
  updateCountdown()
  timer = setInterval(updateCountdown, 1000)
})

onUnmounted(() => {
  clearInterval(timer)
})
</script>

<style scoped>
/* --- Main Counter Section --- */
.hero-wrapper {
  background-image: url('@/assets/wlvcourtyard.jpg');
  background-size: cover;
  background-position: center bottom;
  background-repeat: no-repeat;
  min-height: 100vh;
  padding-top: 150px;
  padding-bottom: 100px;
  display: flex;
  justify-content: center;
  align-items: flex-start;
}

.hero-content {
  background: rgba(255, 255, 255, 0.9);
  padding: 40px;
  border-radius: 12px;
  text-align: center;
  max-width: 700px;
  width: 90%;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.hero-content h1 {
  font-size: 2.8rem;
  font-weight: 800;
  color: #2c3e50;
  margin-bottom: 10px;
}

.hero-subheading {
  font-size: 1.8rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 30px;
}

/* Countdown section vlock styling */
.countdown-wrapper {
  display: flex;
  justify-content: center;
  gap: 20px;
  flex-wrap: wrap;
}
.countdown-item {
  background: white;
  padding: 20px;
  border-radius: 12px;
  min-width: 100px;
  text-align: center;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}
.countdown-number {
  font-size: 2rem;
  font-weight: 700;
  color: #2c3e50;
}
.countdown-label {
  font-size: 1rem;
  color: #7f8c8d;
  margin-top: 5px;
}

/* --- Sections --- */
.section-wrapper {
  padding: 60px 20px;
  display: flex;
  justify-content: center;
  background: #f8f9fa;
}
.section-card {
  background: #fff;
  border-radius: 12px;
  padding: 40px;
  width: 100%;
  max-width: 1000px;
  text-align: center;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}
.wide-card {
  max-width: 1200px;
}

.section-heading {
  font-size: 2.2rem;
  font-weight: 800;
  color: #2c3e50;
  margin-bottom: 20px;
}
.section-description {
  font-size: 1.1rem;
  color: #555;
  margin-bottom: 30px;
}
.button-wrapper {
  margin-top: 20px;
}
.section-button {
  background-color: #ec0d72;
  color: white;
  padding: 12px 30px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 700;
  font-size: 1rem;
  transition: background-color 0.3s ease;
}
.section-button:hover {
  background-color: #c00c60;
}


.video-container {
  position: relative;
  width: 100%;
  padding-bottom: 50%;
  height: 0;
  overflow: hidden;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.video-container iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: 0;
}

/* --- Campuses Section blocks --- */
.campuses-section {
  padding: 80px 20px 50px;
  background: #fff;
  text-align: center;
}
.campuses-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 40px;
  margin-top: 40px;
}
.campus-card {
  width: 320px;
  border-radius: 15px;
  overflow: hidden;
  background: #ffffff;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease-in-out;
}
.campus-card:hover {
  transform: translateY(-5px);
}
.campus-img {
  width: 100%;
  aspect-ratio: 16/9;
  object-fit: cover;
}
.campus-content {
  padding: 20px;
}
.campus-content h2 {
  font-size: 1.8rem;
  color: #2c3e50;
  margin-bottom: 10px;
}
.campus-content p {
  font-size: 1.1rem;
  color: #7f8c8d;
}

/* Mobile tweaks  */
@media (max-width: 768px) {
  .hero-content h1 {
    font-size: 2.2rem;
  }
  .hero-wrapper {
    padding-top: 120px;
    padding-bottom: 80px;
  }
  .hero-subheading {
    font-size: 1.4rem;
  }
}
</style>