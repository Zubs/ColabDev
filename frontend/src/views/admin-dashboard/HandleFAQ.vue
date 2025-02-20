<template>
   <admin-side-bar></admin-side-bar>
   <admin-dashboard-nav-bar> </admin-dashboard-nav-bar>
  <div class="background">
    <div class="container mt-5">
      <h2 class="text-center">FAQ Management</h2>

      <!-- Success & Error Messages -->
      <div v-if="message" class="alert alert-success">{{ message }}</div>
      <div v-if="error" class="alert alert-danger">{{ error }}</div>

      <!-- Added FAQ FORm -->
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
          <li
            v-for="(faq, index) in faqs"
            :key="index"
            class="list-group-item d-flex justify-content-between align-items-center"
          >
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
      </div>

      <!-- Edit FAQ Modal -->
      <div
        v-if="editingFAQ !== null"
        class="modal fade show"
        @click="closeModal"
      >
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
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import AdminSideBar from '@/components/adminSideBar.vue';
import AdminDashboardNavBar from '@/components/AdminDashboardNavBar.vue';

const faqs = ref([
  { question: "Why Is Zubair similar to a certain animal?", answer: "Maybe because he likes bananas." },   //sample data to check if shit is working//
  { question: "What is better Jollof or Biryani?", answer: "Biryani. Let's not be stupid here." }
]);

const newFAQ = ref({ question: "", answer: "" });
const editingFAQ = ref(null);
const editingIndex = ref(null);
const message = ref("");
const error = ref("");

function addFAQ() {
  if (!newFAQ.value.question || !newFAQ.value.answer) {
    error.value = "Question and answer cannot be empty.";
    return;
  }
  faqs.value.push({ ...newFAQ.value });
  newFAQ.value = { question: "", answer: "" };
  message.value = "FAQ added successfully!";
  error.value = "";
}

function editFAQ(index) {
  editingFAQ.value = { ...faqs.value[index] };
  editingIndex.value = index;
}

function updateFAQ() {
  if (!editingFAQ.value.question || !editingFAQ.value.answer) {
    error.value = "Question and answer cannot be empty.";
    return;
  }
  faqs.value[editingIndex.value] = { ...editingFAQ.value };
  editingFAQ.value = null;
  editingIndex.value = null;
  message.value = "FAQ updated successfully!";
  error.value = "";
}

function deleteFAQ(index) {
  if (confirm("Are you sure you want to delete this FAQ?")) {
    faqs.value.splice(index, 1);
    message.value = "FAQ deleted successfully!";
    error.value = "";
  }
}

function closeModal(event) {
  if (event.target.classList.contains("modal")) {
    editingFAQ.value = null;
  }
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
