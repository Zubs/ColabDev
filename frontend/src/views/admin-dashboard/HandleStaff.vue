<template>
  <AdminSideBar />
  <AdminDashboardNavBar />
  <div class="container">
    <div class="row">
      <div class="col-md-2"></div>
      <div class="col-md-10 container">
        <h1>Staffs: {{ staffs.length }} <button class="btn btn-primary float-right" @click="goToCreatePage">Add New Staff</button></h1>
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
                <p>{{ staff.fullname }}</p>
              </td>
              <td>
                <p>{{ staff.username }}</p>
              </td>
              <td>
                <p>{{ staff.email }}</p>
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
import { useRouter } from 'vue-router'

const staffs = ref([])
const router = useRouter()

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

const goToCreatePage = () => {
  router.push({ name: 'admin-staff-create' })
}
</script>
