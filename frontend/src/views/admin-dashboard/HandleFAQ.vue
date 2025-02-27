<template>
  <admin-side-bar></admin-side-bar>
  <admin-dashboard-nav-bar></admin-dashboard-nav-bar>

  <div class="background">
    <div class="container mt-5">
      <h2 class="text-center">FAQ Management</h2>

      <!-- Success & Error Messages -->
      <div v-if="message" class="alert alert-success">{{ message }}</div>
      <div v-if="error" class="alert alert-danger">{{ error }}</div>

      <!--  Add FAQ Modal -->
      <button class="btn btn-primary mb-3" @click="showModal = true">Add New FAQ</button>

      <!-- FAQ List -->
      <div class="card p-3">
        <h5>All FAQs</h5>
        <ul class="list-group">
          <li
            v-for="faq in faqs"
            :key="faq._id"
            class="list-group-item d-flex justify-content-between align-items-center"
          >
            <div>
              <strong>Q:</strong> {{ faq.question }}<br />
              <strong>A:</strong> {{ faq.answer }}
            </div>
            <div>
              <button class="btn btn-warning btn-sm me-2" @click="editFAQ(faq)">Edit</button>
              <button class="btn btn-danger btn-sm" @click="deleteFAQ(faq._id)">Delete</button>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>

  <!-- Add/Edit FAQ Modal -->
  <div v-if="showModal" class="modal fade show d-block" @click="closeModal">
    <div class="modal-dialog modal-lg modal-positioned">
      <div class="modal-content">
        <div class="modal-header">
          <h3 class="modal-title">{{ isEditing ? "Edit FAQ" : "Add New FAQ" }}</h3>
          <button type="button" class="btn-close" @click="closeModal"></button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="isEditing ? updateFAQ() : addFAQ()">
            <div class="mb-3">
              <label class="form-label"><strong>Question</strong></label>
              <input v-model="currentFAQ.question" type="text" class="form-control form-control-lg" required />
            </div>
            <div class="mb-3">
              <label class="form-label"><strong>Answer</strong></label>
              <textarea v-model="currentFAQ.answer" class="form-control form-control-lg" rows="5" required></textarea>
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button type="submit" class="btn btn-primary w-100" @click="isEditing ? updateFAQ() : addFAQ()">
            {{ isEditing ? "Update FAQ" : "Add FAQ" }}
          </button>
          <button type="button" class="btn btn-secondary w-100" @click="closeModal">Cancel</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import axios from "axios";
import AdminSideBar from "@/components/adminSideBar.vue";
import AdminDashboardNavBar from "@/components/AdminDashboardNavBar.vue";

const API_URL = "https://opendaywlvapi.onrender.com/faqs"; // THE FOOLISH MORTAL WHO DARES TO CHANGE THIS SHALL FACE THE WRATH OF THE GODS

const faqs = ref([]); // this stroes the faqs
const currentFAQ = ref({ _id: null, question: "", answer: "" });
const isEditing = ref(false);
const showModal = ref(false);
const message = ref("");
const error = ref("");

// Fetch FAQs 
onMounted(async () => {
  await fetchFAQs();
});

async function fetchFAQs() {
  try {
    const response = await axios.get(API_URL);
    faqs.value = response.data; 
  } catch (err) {
    error.value = "Failed to load FAQs.";
  }
}

async function addFAQ() {
  if (!currentFAQ.value.question || !currentFAQ.value.answer) {
    error.value = "Question and answer cannot be empty.";
    return;
  }
  try {
    const response = await axios.post(API_URL, {
      question: currentFAQ.value.question,
      answer: currentFAQ.value.answer,
    });
    faqs.value.push(response.data); // Adding any new FAQ to the list
    message.value = "FAQ added successfully!";
    closeModal();
  } catch (err) {
    error.value = "Failed to add FAQ.";
  }
}

function editFAQ(faq) {
  isEditing.value = true;
  currentFAQ.value = { ...faq }; 
  showModal.value = true;
}

async function updateFAQ() {
  if (!currentFAQ.value.question || !currentFAQ.value.answer) {
    error.value = "Question and answer cannot be empty.";
    return;
  }
  try {
    await axios.put(`${API_URL}/${currentFAQ.value._id}`, {
      question: currentFAQ.value.question,
      answer: currentFAQ.value.answer,
    });
    const index = faqs.value.findIndex((f) => f._id === currentFAQ.value._id);
    faqs.value[index] = { ...currentFAQ.value }; 
    message.value = "FAQ updated successfully!";
    closeModal();
  } catch (err) {
    error.value = "Failed to update FAQ.";
  }
}

async function deleteFAQ(id) {
  if (!confirm("Are you sure you want to delete this FAQ?")) return;
  try {
    await axios.delete(`${API_URL}/${id}`);
    faqs.value = faqs.value.filter((faq) => faq._id !== id); // Removeing 
    message.value = "FAQ deleted successfully!";
  } catch (err) {
    error.value = "Failed to delete FAQ.";
  }
}

function closeModal() {
  showModal.value = false;
  isEditing.value = false;
  currentFAQ.value = { _id: null, question: "", answer: "" };
}
</script>

<style>
.container {
  max-width: 700px;
}

/* Modal design bullshido */
.modal-dialog {
  display: flex;
  align-items: flex-end;
  justify-content: center;
  min-height: 90vh;
}

/* modal desing bullshido */
.modal-content {
  max-height: 80vh;
  display: flex;
  flex-direction: column;
}

/* modal design bullshido */
.modal-body {
  overflow-y: auto;
  max-height: 60vh;
}

/* modal design bullshido */
.modal-footer {
  position: sticky;
  bottom: 0;
  background: white;
  padding: 15px;
  border-top: 1px solid #ddd;
}
</style>
