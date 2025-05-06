<template>
  <AdminSideBar />
  <AdminDashboardNavBar />
  <div class="container">
    <div class="row">
      <div class="col-md-2"></div>
      <div class="col-md-10 container">
        <h1>
          FAQs: {{ faqs.length }}
          <button class="btn btn-primary float-right" @click="goToCreatePage">Add New FAQ</button>
        </h1>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Data</th>
              <th scope="col"></th>
              <th scope="col"></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(faq, index) in faqs" :key="index">
              <th scope="row">{{ faq.id }}</th>
              <td>
                <p>
                  <strong>Question:</strong> {{ faq.question }} <br />
                  <strong>Answer:</strong> {{ faq.answer }}
                </p>
              </td>
              <td>
                <router-link :to="{ name: 'admin-faqs-edit', params: { id: faq.id } }">
                  <button class="btn btn-warning">Edit</button>
                </router-link>
              </td>
              <td>
                <button class="btn btn-danger" @click="deleteFAQ(faq.id)">Delete</button>
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
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'

const faqs = ref([])
const authStore = useAuthStore()
const router = useRouter()

onMounted(() => {
  fetchFAQs()
})

const fetchFAQs = async () => {
  try {
    const response = await api.get(`/faqs`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    })

    faqs.value = response.data
  } catch (error) {
    if (error.response.status === 401) {
      alert('Sorry, you are not authorized to view this page. Please log in.')
      await authStore.logout()
      await router.push({ name: 'admin-login' })
    }

    console.error('Error fetching FAQs:', error)
  }
}

const goToCreatePage = () => {
  router.push({ name: 'admin-faqs-create' })
}

const deleteFAQ = async (faqId) => {
  if (!confirm('Are you sure you want to delete this faq?')) {
    return // Exit if the user cancels
  }

  try {
    const response = await api.delete(`/faqs/${faqId}`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    })

    if (response.status === 200) {
      alert('Event deleted successfully')
      faqs.value = faqs.value.filter((faq) => faq.id !== faqId)
    }
  } catch (error) {
    console.error('Error deleting FAQ:', error)
    alert('Failed to delete FAQ')
  }
}
</script>
