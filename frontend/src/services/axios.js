import axios from 'axios'

const api = axios.create({
  baseURL: 'https://opendaywlvapi.onrender.com',
  // baseURL: 'http://127.0.0.1:5000',
  headers: { 'Content-Type': 'application/json' },
})

export default api
