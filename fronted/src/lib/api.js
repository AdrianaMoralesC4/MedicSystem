import axios from 'axios'

export const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:3000/api',
  headers: { 'Content-Type': 'application/json' }
})

// Helpers de endpoints (ajusta rutas según tu Tarea 02.03)
export const endpoints = {
  auth: {
    login: (credentials) => api.post('/auth/login', credentials),
  },
  pacientes: {
    list: () => api.get('/pacientes'),
    create: (data) => api.post('/pacientes', data),
    update: (id, data) => api.put(`/pacientes/${id}`, data),
    remove: (id) => api.delete(`/pacientes/${id}`),
  },
  medicos: {
    list: () => api.get('/medicos'),
    create: (data) => api.post('/medicos', data),
    update: (id, data) => api.put(`/medicos/${id}`, data),
    remove: (id) => api.delete(`/medicos/${id}`),
  },
  citas: {
    list: () => api.get('/citas'),
    create: (data) => api.post('/citas', data),
    update: (id, data) => api.put(`/citas/${id}`, data),
    remove: (id) => api.delete(`/citas/${id}`),
  }
}
