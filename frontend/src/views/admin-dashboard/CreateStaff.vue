<template>
  <AdminSideBar />
  <AdminDashboardNavBar />
  <div class="container">
    <div class="row">
      <div class="col-md-2"></div>
      <div class="col-md-10 container">
        <h1>Create New Staff</h1>
        <form class="contact-form w-100" @submit.prevent="createStaff">
          <div class="form-row">
            <div class="form-group col-md-6">
              <label for="username">Username</label>
              <input
                type="text"
                class="form-control"
                id="username"
                placeholder="Username"
                v-model="staff.username"
                @input="validateUsername"
              />
              <span v-if="errors.username" class="text-danger">{{ errors.username }}</span>
            </div>
            <div class="form-group col-md-6">
              <label for="fullname">Fullname</label>
              <input
                type="text"
                class="form-control"
                id="fullname"
                placeholder="Fullname"
                v-model="staff.fullname"
              />
              <span v-if="errors.fullname" class="text-danger">{{ errors.fullname }}</span>
            </div>
          </div>
          <div class="form-row">
            <div class="form-group col-md-6">
              <label for="password">Password</label>
              <input
                type="password"
                class="form-control"
                id="password"
                placeholder="Password"
                v-model="staff.password"
              />
              <span v-if="errors.password" class="text-danger">{{ errors.password }}</span>
            </div>
            <div class="form-group col-md-6">
              <label for="email">Email</label>
              <input
                type="text"
                class="form-control"
                id="email"
                placeholder="Email"
                v-model="staff.email"
              />
              <span v-if="errors.email" class="text-danger">{{ errors.email }}</span>
            </div>
          </div>
          <div class="form-group text-center">
            <button type="submit" class="btn btn-primary px-5 form-control" :disabled="loading">
              <span v-if="loading">Processing...</span>
              <span v-else>Create Staff</span>
            </button>
            <span v-if="errors.request" class="text-danger">{{ errors.request }}</span>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import AdminDashboardNavBar from '../../components/AdminDashboardNavBar.vue'
import AdminSideBar from '@/components/AdminSideBar.vue'
import { ref } from 'vue'
import api from '@/services/axios.js'
import { useRouter } from 'vue-router'

const staff = ref({
  fullname: '',
  username: '',
  password: '',
  email: '',
})
const errors = ref({
  fullname: '',
  username: '',
  password: '',
  email: '',
  request: '',
})
const loading = ref(false)
const router = useRouter()

const validateUsername = () => {
  if (!staff.value.username) {
    errors.value.username = 'Username is required'
  } else if (staff.value.username.length < 5) {
    errors.value.username = 'Username must be at least 5 characters'
  } else {
    errors.value.username = ''
  }
}

const validate = () => {
  errors.value = {
    fullname: '',
    username: '',
    password: '',
    email: '',
    request: '',
  }

  validateUsername()

  if (!staff.value.fullname) {
    errors.value.fullname = 'Full name is required'
  }

  if (!staff.value.password) {
    errors.value.password = 'Password is required'
  }

  if (!staff.value.email) {
    errors.value.email = 'Email is required'
  }

  return (
    !errors.value.username &&
    !errors.value.password &&
    !errors.value.fullname &&
    !errors.value.email
  )
}

const createStaff = async () => {
  if (!validate()) return

  loading.value = true

  try {
    await api.post(`/auth/register`, staff.value)
    loading.value = false
    await router.push({ name: 'admin-staff' })
  } catch (error) {
    console.error('Error creating staff:', error)
    errors.value.request = `Failed to create staff: ${error.response.data.error || error.message}`
    loading.value = false
  }
}
</script>
