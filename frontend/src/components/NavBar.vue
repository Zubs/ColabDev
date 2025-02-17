<template>
  <nav class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
    <div class="container">
      <a class="navbar-brand" href="/"><img src="https://www.wlv.ac.uk/media/2019-template-assets/graphics/logo.svg" alt="University Of Wolverhampton Logo"></a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#ftco-nav" aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="oi oi-menu"></span> Menu
      </button>

      <div class="collapse navbar-collapse" id="ftco-nav">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item" :class="{ active: route.name === 'home' }"><a href="/" class="nav-link">Home</a></li>
          <li class="nav-item" :class="{ active: route.name === 'about' }"><a href="/about" class="nav-link">About</a></li>
          <li class="nav-item" :class="{ active: route.name === 'events' }"><a href="/events" class="nav-link">Events Schedule</a></li>
          <li class="nav-item" :class="{ active: route.name === 'blog' }"><a href="/blog" class="nav-link">Blog</a></li>
          <li class="nav-item" :class="{ active: route.name === 'faqs' }"><a href="/faqs" class="nav-link">FAQ's</a></li>
          <li class="nav-item" :class="{ active: route.name === 'admin-login' }"><a href="/admin/login" class="nav-link">Admin login</a></li>
          <li class="nav-item cta mr-md-2"><a href="/registration" class="nav-link">Book Now</a></li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
</script>
