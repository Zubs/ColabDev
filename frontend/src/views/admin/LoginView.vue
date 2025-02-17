<template>
  <NavBar />
  <section>
    <section class="mt-20">
      <div class="overlay"></div>
      <div class="container">
        <div class="row no-gutters slider-text align-items-end justify-content-start">
          <div class="col-md-9 ftco-animate pb-5 fadeInUp ftco-animated">
            <!-- Added inline style to the h1 tag for top margin -->
            <h1 class="mb-3 bread" style="margin-top: 150px;">UoW Admin Login</h1>
            <p class="breadcrumbs"><span class="mr-2"><a href="index.html">Home <i class="ion-ios-arrow-forward"></i></a></span> <span>Contact <i class="ion-ios-arrow-forward"></i></span></p>
          </div>
        </div>
      </div>
    </section>
    <div class="row block-9">
      <div class="col-md-6 order-md-last d-flex">
        <form action="#" class="bg-light p-5 contact-form" style="width: 65%; max-width: 600px; padding: 50px; margin-left: 100px;">

          <div class="form-group" style="width: 100%; max-width: 1000px;">
            <input type="text" class="form-control" placeholder="Username" style="width:100%; max-width: 1000px;">
          </div>
          <div class="form-group">
            <input type="text" class="form-control" placeholder="Password">
          </div>
          <div class="form-group">
            <input type="submit" value="Login!" class="btn btn-primary py-3 px-5">
          </div>
          <button type="button" class="btn btn-link" style="margin-left: -11px;"> <!--<a href=link class=......> </a>-->
            Forgot Password?
          </button>


        </form>


      </div>

      <div class="col-md-6 d-flex">
        <img src="https://cdn-wlvacuk.terminalfour.net/media/departments/digital-content-and-communications/images-18-19/DSC_0103.JPG" alt="Responsive image" class="img-fluid" style="margin-left: 150px;">
      </div>
    </div>
  </section>

    <div class="overlay"></div>
    <div class="container">
      <div class="row no-gutters slider-text js-fullheight align-items-end justify-content-start">
        <div class="col-md-9 ftco-animate pb-5">
          <p class="breadcrumbs"><span class="mr-2"><a href="index.html">Home <i class="ion-ios-arrow-forward"></i></a></span> <span>Contact <i class="ion-ios-arrow-forward"></i></span></p>
        </div>
      </div>
    </div>

  <Footer />
</template>
<script setup lang="ts">
import NavBar from '@/components/NavBar.vue'
import Footer from '@/components/Footer.vue'
</script>
