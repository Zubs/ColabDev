<template>
  <AdminSideBar />
  <AdminDashboardNavBar />
  <div class="container">
    <div class="row">
      <div class="col-md-2"></div>
      <div class="col-md-10 container">
        <h1>Create New FAQ</h1>
        <form class="contact-form w-100" @submit.prevent="createFAQ">
          <div class="form-row">
            <div class="form-group col-md-12">
              <label for="question">Question</label>
              <input
                type="text"
                class="form-control"
                id="question"
                placeholder="Question"
                v-model="faq.question"
              />
              <span v-if="errors.question" class="text-danger">{{ errors.question }}</span>
            </div>
          </div>
          <div class="form-row">
            <div class="form-group col-md-12">
              <label for="answer">Answer</label>
              <textarea
                class="form-control"
                id="answer"
                placeholder="Answer"
                v-model="faq.answer"
              ></textarea>
              <span v-if="errors.answer" class="text-danger">{{ errors.answer }}</span>
            </div>
          </div>
          <div class="form-group text-center">
            <button type="submit" class="btn btn-primary px-5 form-control" :disabled="loading">
              <span v-if="loading">Processing...</span>
              <span v-else>Create FAQ</span>
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

const faq = ref({
  question: '',
  answer: '',
})
const errors = ref({
  question: '',
  answer: '',
  request: '',
})
const loading = ref(false)
const router = useRouter()

const validate = () => {
  errors.value = {
    question: '',
    answer: '',
    request: '',
  }

  if (!faq.value.question) {
    errors.value.question = 'Question is required'
  }

  if (!faq.value.answer) {
    errors.value.answer = 'Answer is required'
  }

  return !errors.value.question && !errors.value.answer
}

const createFAQ = async () => {
  if (!validate()) return

  loading.value = true

  try {
    await api.post(`/faqs`, faq.value, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    })

    loading.value = false
    await router.push({ name: 'admin-faqs' })
  } catch (error) {
    console.error('Error creating FAQ:', error)
    errors.value.request = `Failed to create FAQ: ${error.response.data.error || error.message}`
    loading.value = false
  }
}
</script>
