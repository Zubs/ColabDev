import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import api from '@/services/axios'

export const useAuthStore = defineStore('auth', () => {
  const user = ref(JSON.parse(localStorage.getItem('user')) || null)
  const token = ref(localStorage.getItem('token') || null)

  const isAuthenticated = computed(() => !!user.value && !!token.value)

  const login = async (credentials) => {
    try {
      const response = await api.post('/auth/login', credentials)

      console.log('Login response:')
      console.log(response)

      if (response.data.data.error || !response.data.data.user || !response.data.data.token) {
        throw new Error('Unable to login')
      }

      user.value = response.data.data.user
      token.value = response.data.data.token
      localStorage.setItem('user', JSON.stringify(user.value))
      localStorage.setItem('token', token.value)
    } catch (error) {
      console.error('Login failed:', error)
      throw error
    }
  }

  const logout = async () => {
    try {
      const response = await api.post('/auth/logout', credentials)
      user.value = null
      token.value = null
      localStorage.removeItem('user')
      localStorage.removeItem('token')
    } catch (error) {
      console.error('Login failed:', error)
      throw error
    }
  }

  return { user, token, isAuthenticated, login, logout }
})
