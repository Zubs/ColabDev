<template>
  <NavBar />
  <section>
    <section class="mt-20">
      <div class="overlay"></div>
      <div class="container">
        <div class="row no-gutters slider-text align-items-end justify-content-start">
          <div class="col-md-9 ftco-animate pb-5 fadeInUp ftco-animated">
            <!-- Added inline style to the h1 tag for top margin -->
            <h1 class="mb-3 bread" style="margin-top: 150px">UoW Admin Login</h1>
            <p class="breadcrumbs">
              <span class="mr-2"
              ><a href="/">Home <i class="ion-ios-arrow-forward"></i></a
              ></span>
              <span>Admin Login <i class="ion-ios-arrow-forward"></i></span>
            </p>
          </div>
        </div>
        <div class="row container">
          <div class="col-md-6 order-md-last bg-light">
            <form @submit.prevent="login" class="bg-light p-5 contact-form">
              <div class="form-group">
                <input
                  v-model="username"
                  @input="validateUsername"
                  type="text"
                  class="form-control"
                  placeholder="Username"
                />
                <span v-if="errors.username" class="text-danger">{{ errors.username }}</span>
              </div>
              <div class="form-group">
                <input
                  v-model="password"
                  type="password"
                  class="form-control"
                  placeholder="Password"
                />
                <span v-if="errors.password" class="text-danger">{{ errors.password }}</span>
              </div>
              <div class="form-group">
                <input
                  type="submit"
                  value="Login"
                  class="btn btn-primary py-3 px-5 form-control"
                  :disabled="loading"
                />
                <span v-if="loading" class="text-info">Loading...</span>
                <span v-if="errors.request" class="text-danger">{{ errors.request }}</span>
              </div>
            </form>
          </div>
          <div class="col-md-6 bg-light">
            <img
              src="https://cdn-wlvacuk.terminalfour.net/media/departments/digital-content-and-communications/images-18-19/DSC_0103.JPG"
              alt="Responsive image"
              class="img-fluid"
            />
          </div>
        </div>
      </div>
    </section>
  </section>
  <div class="container">
    <div class="row no-gutters slider-text js-fullheight align-items-end justify-content-start">
      <div class="col-md-9 ftco-animate pb-5">
        <p class="breadcrumbs">
          <span class="mr-2"
          ><a href="/">Home <i class="ion-ios-arrow-forward"></i></a
          ></span>
          <span>Contact <i class="ion-ios-arrow-forward"></i></span>
        </p>
      </div>
    </div>
  </div>
  <Footer />
</template>

<script setup lang="ts">
import { ref } from 'vue'
import NavBar from '@/components/NavBar.vue'
import Footer from '@/components/Footer.vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'

const username = ref('')
const password = ref('')
const errors = ref({ username: '', password: '', request: '' })
const loading = ref(false)
const authStore = useAuthStore()
const router = useRouter()

const validateUsername = () => {
  errors.value.username = ''
  if (!username.value) {
    errors.value.username = 'Username is required'
  } else if (username.value.length < 5) {
    errors.value.username = 'Username must be at least 5 characters'
  }
}

const validate = () => {
  validateUsername()
  errors.value.password = ''
  if (!password.value) {
    errors.value.password = 'Password is required'
  }
  return !errors.value.username && !errors.value.password
}

const login = async () => {
  if (!validate()) return
  loading.value = true
  errors.value.request = ''

  try {
    await authStore.login({ username: username.value, password: password.value })
    await router.push({ name: 'admin-dashboard' })
  } catch (error) {
    errors.value.request = `Login failed: ${error.response.data.error || error.message}`
  }

  loading.value = false
}
</script>
