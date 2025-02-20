<template>
  <div class="faq-admin">
    <h1>Admin Dashboard: Manage FAQs</h1>

    <form @submit.prevent="handleSubmit">
      <div>
        <label for="question">Question:</label>
        <input
          type="text"
          id="question"
          v-model="faqForm.question"
          required
        />
      </div>
      <div>
        <label for="answer">Answer:</label>
        <textarea
          id="answer"
          v-model="faqForm.answer"
          required
        ></textarea>
      </div>
      <button type="submit">{{ isEditing ? 'Update' : 'Add' }} FAQ</button>
    </form>

    <h2>FAQs</h2>
    <ul>
      <li v-for="(faq, index) in faqs" :key="index">
        <strong>{{ faq.question }}</strong>: {{ faq.answer }}
        <button @click="editFaq(index)">Edit</button>
        <button @click="removeFaq(index)">Remove</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      faqs: [],
      faqForm: {
        question: '',
        answer: '',
      },
      isEditing: false,
      editingIndex: null,
    };
  },
  methods: {
    handleSubmit() {
      if (this.isEditing) {
        this.faqs[this.editingIndex] = { ...this.faqForm };
      } else {
        this.faqs.push({ ...this.faqForm });
      }
      this.resetForm();
    },
    editFaq(index) {
      this.faqForm = { ...this.faqs[index] };
      this.isEditing = true;
      this.editingIndex = index;
    },
    removeFaq(index) {
      this.faqs.splice(index, 1);
    },
    resetForm() {
      this.faqForm.question = '';
      this.faqForm.answer = '';
      this.isEditing = false;
      this.editingIndex = null;
    },
  },
};
</script>

<style scoped>
.faq-admin {
  max-width: 600px;
  margin: auto;
}

form {
  margin-bottom: 20px;
}
</style>
