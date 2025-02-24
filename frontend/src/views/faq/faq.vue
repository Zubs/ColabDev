<template>
  <div>
    <NavBar />
    <div class="background-container">
      <section class="content">
        <div class="faq-container">
          <h1 class="move-rightheader">University Open Day - FAQ</h1>
          <div v-for="(item, index) in faqs" :key="index" class="faq-item">
            <div class="question" @click="toggleFAQ(index)">
              {{ item.question }}
              <span class="icon">{{ item.open ? '▲' : '▼' }}</span>
            </div>
            <div class="answer" :class="{ show: item.open }">
              {{ item.answer }}
            </div>
          </div>
        </div>
      </section>
    </div>
    <Footer />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import NavBar from '@/components/NavBar.vue'
import Footer from '@/components/Footer.vue'
import { onMounted } from 'vue'
import api from '@/services/axios.js'

const faqs = ref([])

const fetchFAQs = async () => {
  try {
    const response = await api.get(`/faqs`)
    faqs.value = response.data
  } catch (error) {
    console.error('Error fetching FAQs:', error)
  }
}

onMounted(() => {
  fetchFAQs()
})

const toggleFAQ = (index) => {
  faqs.value[index].open = !faqs.value[index].open
}
</script>

<style scoped>
.background-container {
  /* Background container with an image (DONOT MAKE ANY CHANGES TOOK ME 6 YEARS SOMEHOW TO GET THE BACKGROUND IMAGE)*/
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  padding-top: 100px;
  z-index: 0;
  background-image: url(MCbuilding.jpeg);
  background-size: cover;
  background-position: center;
}

.background-container::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: inherit;
  background-size: cover;
  background-position: center;
  filter: blur(5px);
  z-index: -1;
}

.faq-container {
  width: 95%;
  max-width: 1100px;
  background: rgba(255, 255, 255, 0.85);
  padding: 60px;
  border-radius: 12px;
  box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.15);
  margin: 100px auto;
  text-align: center;
}

h1 {
  color: #333;
  font-size: 3rem;
  font-weight: bold;
  margin-bottom: 30px;
}

.faq-item {
  border-bottom: 1px solid #ddd;
  padding: 20px;
  transition: all 0.3s ease-in-out;
  width: 100%;
  max-width: 1000px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
}

.question {
  font-size: 26px;
  font-weight: bold;
  cursor: pointer;
  padding: 25px 50px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #f9f9f9;
  border-radius: 10px;
  transition: background 0.3s;
  width: 100%;
  text-align: left;
}

.question:hover {
  background-color: #e0e0e0;
}

.answer {
  opacity: 0;
  visibility: hidden;
  transition:
    opacity 0.3s ease-in-out,
    visibility 0.3s ease-in-out;
  padding: 0 50px;
  text-align: left;
  font-size: 20px;
  height: 0;
  overflow: hidden;
  display: flex;
  align-items: center;
}

.answer.show {
  opacity: 1;
  visibility: visible;
  height: auto;
  padding: 15px 50px;
}

.icon {
  font-size: 30px;
  transition: transform 0.3s;
}
</style>
