import axios from 'axios'

const api = axios.create({
  baseURL: 'https://opendaywlvapi.onrender.com', // Change to your API URL
  headers: { 'Content-Type': 'application/json' },
})

export default api
