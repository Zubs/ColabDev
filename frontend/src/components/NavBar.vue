<template>
  <nav
    class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light"
    id="ftco-navbar"
  >
    <div class="container">
      <router-link class="navbar-brand" :to="{ name: 'home' }">
        <img
          src="https://www.wlv.ac.uk/media/2019-template-assets/graphics/logo.svg"
          alt="University Of Wolverhampton Logo"
        />
      </router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#ftco-nav"
        aria-controls="ftco-nav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="oi oi-menu"></span> Menu
      </button>
      <div class="collapse navbar-collapse" id="ftco-nav">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item" :class="{ active: route.name === 'home' }">
            <router-link :to="{ name: 'home' }" class="nav-link">Home</router-link>
          </li>
          <li class="nav-item" :class="{ active: route.name === 'events' }">
            <router-link to="/events" class="nav-link">Events Schedule</router-link>
          </li>
          <li class="nav-item" :class="{ active: route.name === 'faqs' }">
            <router-link :to="{ name: 'faqs' }" class="nav-link">FAQ's</router-link>
          </li>
          <li class="nav-item" :class="{ active: route.name === 'admin-login' }">
            <router-link :to="{ name: 'admin-login' }" class="nav-link">Admin login</router-link>
          </li>
          <li class="nav-item cta mr-md-2">
            <router-link :to="{ name: 'registration' }" class="nav-link">Book Now</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
</script>

<style scoped>
@media (max-width: 768px) {
  .navbar-nav .nav-link {
    color: white !important;
  }
}
</style>
