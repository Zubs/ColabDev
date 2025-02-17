<template>
  <div class="hero-wrap js-fullheight" style="background-image: url('/images/bg_1.jpg');" data-stellar-background-ratio="0.5">
    <div class="overlay"></div>
    <div class="container">
      <div class="row no-gutters slider-text js-fullheight align-items-center justify-content-start" data-scrollax-parent="true">
        <div class="col-xl-10 ftco-animate" data-scrollax=" properties: { translateY: '70%' }">
          <h1 class="mb-4" data-scrollax="properties: { translateY: '30%', opacity: 1.6 }" style="opacity: 1;
    transform: translateZ(0px) translateY(0%);"> Undergraduate <br><span>Open Day</span></h1>
          <p class="mb-4" data-scrollax="properties: { translateY: '30%', opacity: 1.6 }">SATURDAY 15 MARCH, 11:00 AM - 2:30 PM</p>
          <div id="timer" class="d-flex mb-3">
            <div class="time" id="days"></div>
            <div class="time pl-4" id="hours"></div>
            <div class="time pl-4" id="minutes"></div>
            <div class="time pl-4" id="seconds"></div>
          </div>
          <a href="/registration" class="btn btn-primary btn-lg mt-5">Book Now</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import {onMounted} from "vue";

onMounted(() => {
  console.log(window.$);
});
</script>
