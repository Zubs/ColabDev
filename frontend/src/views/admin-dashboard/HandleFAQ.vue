<<template>
  <admin-side-bar></admin-side-bar>
  <admin-dashboard-nav-bar></admin-dashboard-nav-bar>

  <div class="background">
    <div class="container mt-5">
      <h1 class="text-center">FAQ Management</h1>

      <!-- Success & Error Messages -->
      <div v-if="message" class="alert alert-success">{{ message }}</div>
      <div v-if="error" class="alert alert-danger">{{ error }}</div>

      <!-- Add FAQ Button -->
      <button class="btn btn-primary mb-3" @click="openAddModal">Add New FAQ</button>

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
              <button class="btn btn-warning btn-sm me-2" @click="openEditModal(faq)">Edit</button>
              <button class="btn btn-danger btn-sm" @click="deleteFAQ(faq._id)">Delete</button>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>

  <!-- Add/Edit FAQ Modal -->
  <div v-if="showModal" class="modal fade show d-block" @click="closeModal">
    <div class="modal-dialog modal-lg modal-positioned" @click.stop>
      <div class="modal-content">
        <div class="modal-header">
          <h3 class="modal-title">{{ isEditing ? "Edit FAQ" : "Add New FAQ" }}</h3>
          <button type="button" class="btn-close" @click="closeModal"></button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="handleSubmit">
            <div class="mb-3">
              <label class="form-label"><strong>Question</strong></label>
              <input v-model="currentFAQ.question" type="text" class="form-control form-control-lg" required />
            </div>
            <div class="mb-3">
              <label class="form-label"><strong>Answer</strong></label>
              <textarea v-model="currentFAQ.answer" class="form-control form-control-lg" rows="5" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary w-100">
              {{ isEditing ? "Update FAQ" : "Add FAQ" }}
            </button>
          </form>
        </div>
        <div class="modal-footer">
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

const API_URL = "https://opendaywlvapi.onrender.com/faqs";

const faqs = ref([]); // Stores the FAQs
const currentFAQ = ref({ _id: null, question: "", answer: "" });
const isEditing = ref(false);
const showModal = ref(false);
const message = ref("");
const error = ref("");

// Fetch FAQs when page loads too slow
onMounted(fetchFAQs);

async function fetchFAQs() {
  try {
    const response = await axios.get(API_URL);
    faqs.value = response.data;
    console.log("Fetched FAQs:", faqs.value);
  } catch (err) {
    error.value = "Failed to load FAQs.";
    console.error("Fetch FAQs Error:", err);
  }
}

// Open Add FAQ Modal 
function openAddModal() {
  isEditing.value = false;
  currentFAQ.value = { _id: null, question: "", answer: "" };
  showModal.value = true;
}

// Open Edit FAQ Modal
function openEditModal(faq) {
  isEditing.value = true;
  currentFAQ.value = { ...faq };
  showModal.value = true;
}

// Handle Submit for Add or Update [trash]
async function handleSubmit() {
  if (!currentFAQ.value.question.trim() || !currentFAQ.value.answer.trim()) {
    error.value = "Question and answer cannot be empty.";
    return;
  }

  try {
    if (isEditing.value) {
      await updateFAQ();
    } else {
      await addFAQ();
    }
  } catch (err) {
    error.value = err.response?.data?.message || "Failed to process request.";
  }
}

// Add New FAQ all good
async function addFAQ() {
  try {
    const response = await axios.post(API_URL, {
      question: currentFAQ.value.question.trim(),
      answer: currentFAQ.value.answer.trim(),
    });

    message.value = "FAQ added successfully!";
    closeModal();
    fetchFAQs(); // Refresh list after adding
  } catch (err) {
    console.error("Add FAQ Error:", err.response?.data || err);
    error.value = err.response?.data?.message || "Failed to add FAQ.";
  }
}

// Update FAQ [trash]
async function updateFAQ() {
  if (!currentFAQ.value._id) {
    error.value = "Invalid FAQ ID. Cannot update.";
    return;
  }

  try {
    await axios.put(`${API_URL}/${currentFAQ.value._id}`, {
      question: currentFAQ.value.question.trim(),
      answer: currentFAQ.value.answer.trim(),
    });

    message.value = "FAQ updated successfully!";
    closeModal();
    fetchFAQs(); // Refresh list after update
  } catch (err) {
    console.error("Update FAQ Error:", err.response?.data || err);
    error.value = err.response?.data?.message || "Failed to update FAQ.";
  }
}

// Delete FAQ [trash]
async function deleteFAQ(id) {
  if (!confirm("Are you sure you want to delete this FAQ?")) return;

  try {
    await axios.delete(`${API_URL}/${id}`);
    message.value = "FAQ deleted successfully!";
    fetchFAQs(); // Refresh list after deleting
  } catch (err) {
    console.error("Delete FAQ Error:", err.response?.data || err);
    error.value = err.response?.data?.message || "Failed to delete FAQ.";
  }
}

// Close Modal & Reset Form
function closeModal() {
  showModal.value = false;
  isEditing.value = false;
  currentFAQ.value = { _id: null, question: "", answer: "" };
  message.value = "";
  error.value = "";
}
</script>

<style>
.container {
  max-width: 700px;
}
.modal-dialog {
  display: flex;
  align-items: flex-end;
  justify-content: center;
  min-height: 90vh;
}
.modal-content {
  max-height: 80vh;
  display: flex;
  flex-direction: column;
}
.modal-body {
  overflow-y: auto;
  max-height: 60vh;
}
.modal-footer {
  position: sticky;
  bottom: 0;
  background: white;
  padding: 15px;
  border-top: 1px solid #ddd;
}
</style>

