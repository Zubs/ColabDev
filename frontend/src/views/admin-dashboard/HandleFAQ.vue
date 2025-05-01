<template>
  <AdminSideBar />
  <AdminDashboardNavBar />
  <div class="container mt-4">
    <div class="row">
      <div class="col-md-2"></div>
      <div class="col-md-10">
        <div class="d-flex justify-content-between align-items-center mb-3">
          <h1 class="mb-0">FAQs: {{ faqs.length }}</h1>
          <button class="btn btn-primary" @click="goToCreatePage">Add New FAQ</button>
        </div>

        <table class="table table-hover">
          <thead>
            <tr>
              <th>#</th>
              <th>Data</th>
              <th></th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="faq in faqs" :key="faq.id">
              <th scope="row">{{ faq.id }}</th>
              <td>
                <p class="mb-1">
                  <strong>Question:</strong> {{ faq.question }}
                </p>
                <p class="mb-0">
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
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/services/axios.js'
import { useAuthStore } from '@/stores/auth'
import AdminDashboardNavBar from '@/components/AdminDashboardNavBar.vue'
import AdminSideBar from '@/components/AdminSideBar.vue'

const faqs = ref([])
const router = useRouter()
const authStore = useAuthStore()

const fetchFAQs = async () => {
  try {
    const response = await api.get('/faqs', {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    })
    faqs.value = response.data
  } catch (error) {
    if (error.response?.status === 401) {
      alert('You are not authorized. Redirecting to login.')
      await authStore.logout()
      router.push({ name: 'admin-login' })
    }
    console.error('Error fetching FAQs:', error)
  }
}

const goToCreatePage = () => {
  router.push({ name: 'admin-faqs-create' })
}

const deleteFAQ = async (faqId: number) => {
  if (!confirm('Are you sure you want to delete this FAQ?')) return

  try {
    const response = await api.delete(`/faqs/${faqId}`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    })

    if (response.status === 200) {
      faqs.value = faqs.value.filter(faq => faq.id !== faqId)
      alert('FAQ deleted successfully')
    }
  } catch (error) {
    console.error('Error deleting FAQ:', error)
    alert('Failed to delete FAQ')
  }
}

onMounted(fetchFAQs)
</script>
