<template>
  <div class="container mt-5">
    <h2 class="text-center">FAQ Management</h2>

    <!-- Success & Error Messages -->
    <div v-if="message" class="alert alert-success">{{ message }}</div>
    <div v-if="error" class="alert alert-danger">{{ error }}</div>

    <!-- Add FAQ Form -->
    <div class="card p-3 mt-3">
      <h5>Add New FAQ</h5>
      <form @submit.prevent="addFAQ">
        <div class="mb-3">
          <label class="form-label">Question</label>
          <input v-model="newFAQ.question" type="text" class="form-control" required />
        </div>
        <div class="mb-3">
          <label class="form-label">Answer</label>
          <textarea v-model="newFAQ.answer" class="form-control" rows="3" required></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Add FAQ</button>
      </form>
    </div>

    <!-- FAQ List -->
    <div class="card p-3 mt-4">
      <h5>All FAQs</h5>
      <ul class="list-group">
        <li v-for="(faq, index) in faqs" :key="index" class="list-group-item d-flex justify-content-between align-items-center">
          <div>
            <strong>Q:</strong> {{ faq.question }}<br />
            <strong>A:</strong> {{ faq.answer }}
          </div>
          <div>
            <button class="btn btn-warning btn-sm me-2" @click="editFAQ(index)">Edit</button>
            <button class="btn btn-danger btn-sm" @click="deleteFAQ(index)">Delete</button>
          </div>
        </li>
      </ul>
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
      <div class="col-md-6 d-flex">
        <img
          src="https://cdn-wlvacuk.terminalfour.net/media/departments/digital-content-and-communications/images-18-19/DSC_0103.JPG"
          alt="Responsive image"
          class="img-fluid"
          style="margin-left: 150px"
        />
      </div>
    </div>

    <!-- Edit FAQ Modal -->
    <div v-if="editingFAQ !== null" class="modal fade show" style="display: block; background: rgba(0, 0, 0, 0.5);" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Edit FAQ</h5>
            <button type="button" class="btn-close" @click="editingFAQ = null"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="updateFAQ">
              <div class="mb-3">
                <label class="form-label">Question</label>
                <input v-model="editingFAQ.question" type="text" class="form-control" required />
              </div>
              <div class="mb-3">
                <label class="form-label">Answer</label>
                <textarea v-model="editingFAQ.answer" class="form-control" rows="3" required></textarea>
              </div>
              <button type="submit" class="btn btn-success">Update FAQ</button>
              <button type="button" class="btn btn-secondary ms-2" @click="editingFAQ = null">Cancel</button>
            </form>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>
<script>
export default {
  data() {
    return {
      faqs: [
        { question: "Why Is Zubair similiar to a certain animal?", answer: "Maybe because he likes bananas." },
        { question: "What is better Jollof or Biryani?", answer: "Biryani Let's not be stupid here." }
      ],
      newFAQ: { question: "", answer: "" },
      editingFAQ: null,
      editingIndex: null,
      message: "",
      error: ""
    };
  },
  methods: {
    addFAQ() {
      if (!this.newFAQ.question || !this.newFAQ.answer) {
        this.error = "Question and answer cannot be empty.";
        return;
      }
      this.faqs.push({ ...this.newFAQ });
      this.newFAQ = { question: "", answer: "" };
      this.message = "FAQ added successfully!";
      this.error = "";
    },
    editFAQ(index) {
      this.editingFAQ = { ...this.faqs[index] };
      this.editingIndex = index;
    },
    updateFAQ() {
      if (!this.editingFAQ.question || !this.editingFAQ.answer) {
        this.error = "Question and answer cannot be empty.";
        return;
      }
      this.faqs[this.editingIndex] = { ...this.editingFAQ };
      this.editingFAQ = null;
      this.editingIndex = null;
      this.message = "FAQ updated successfully!";
      this.error = "";
    },
    deleteFAQ(index) {
      if (confirm("Are you sure you want to delete this FAQ?")) {
        this.faqs.splice(index, 1);
        this.message = "FAQ deleted successfully!";
        this.error = "";
      }
    }

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

<style>
.container {
  max-width: 700px;
}
.modal {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 1050;
}
</style>
