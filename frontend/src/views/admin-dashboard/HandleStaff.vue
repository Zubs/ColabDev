<template>
  <AdminSideBar />
  <AdminDashboardNavBar />
  <div class="container">
    <div class="row">
      <div class="col-md-2"></div>
      <div class="col-md-10 container">
        <h1>Staffs: {{ staffs.length }}</h1>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Fullname</th>
              <th scope="col">Username</th>
              <th scope="col">Email</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(staff, index) in staffs" :key="index">
              <th scope="row">{{ staff.id }}</th>
              <td>
                <p><strong>Full Name:</strong> {{ staff.fullname }}</p>
              </td>
              <td>
                <p><strong>Username:</strong> {{ staff.username }}</p>
              </td>
              <td>
                <p><strong>Email:</strong> {{ staff.email }}</p>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import AdminDashboardNavBar from '../../components/AdminDashboardNavBar.vue'
import AdminSideBar from '@/components/AdminSideBar.vue'
import { onMounted, ref } from 'vue'
import api from '@/services/axios.js'

const staffs = ref([])

onMounted(() => {
  fetchStaffs()
})

const fetchStaffs = async () => {
  try {
    const response = await api.get(`/auth/users`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    })
    staffs.value = response.data
  } catch (error) {
    console.error('Error fetching Staff:', error)
  }
}
</script>
