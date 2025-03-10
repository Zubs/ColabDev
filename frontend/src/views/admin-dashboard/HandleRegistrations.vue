<template>
  <AdminSideBar />
  <AdminDashboardNavBar />
  <div class="container">
    <div class="row">
      <div class="col-md-2"></div>
      <div class="col-md-10 container">
        <h1>Registrations: {{ registrations.length }}</h1>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Data</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(registration, index) in registrations" :key="index">
              <th scope="row">{{ registration.id }}</th>
              <td>
                <p>
                  <strong>Full Name:</strong> {{ registration.title }} {{ registration.last_name }}
                  {{ registration.first_name }}
                </p>
                <p>
                  <strong>Address:</strong> {{ registration.address_line1 }},
                  {{ registration.address_line2 }}, {{ registration.city }},
                  {{ registration.country }}, {{ registration.postcode }}
                </p>
                <p><strong>Date of Birth:</strong> {{ registration.date_of_birth }}</p>
                <p><strong>Email:</strong> {{ registration.email }}</p>
                <p><strong>Event Date:</strong> {{ registration.event_date }}</p>
                <p v-if="registration.guest_count">
                  <strong>Guest Count:</strong> {{ registration.guest_count }}
                </p>
                <p><strong>Level of Study:</strong> {{ registration.level_of_study }}</p>
                <p>
                  <strong>Marketing Sources:</strong>
                  {{ registration.marketing_sources.join(', ') }}
                </p>
                <p><strong>Phone Number:</strong> {{ registration.phone_number }}</p>
                <p><strong>Subject Area:</strong> {{ registration.subject_area }}</p>
                <p v-if="registration.carer_email">
                  <strong>Carer Email:</strong> {{ registration.carer_email }}
                </p>
                <p v-if="registration.carer_first_name">
                  <strong>Carer First Name:</strong> {{ registration.carer_first_name }}
                </p>
                <p v-if="registration.carer_last_name">
                  <strong>Carer Last Name:</strong> {{ registration.carer_last_name }}
                </p>
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

const registrations = ref([])

onMounted(() => {
  fetchRegistrations()
})

const fetchRegistrations = async () => {
  try {
    const response = await api.get(`/registration`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    })
    registrations.value = response.data
  } catch (error) {
    console.error('Error fetching Registrations:', error)
  }
}
</script>
