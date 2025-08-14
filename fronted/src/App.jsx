import { Routes, Route, Navigate } from 'react-router-dom'
import Login from './pages/Login.jsx'
import Dashboard from './pages/Dashboard.jsx'
import Patients from './pages/Patients.jsx'
import Doctors from './pages/Doctors.jsx'
import Appointments from './pages/Appointments.jsx'
import Users from './pages/Users.jsx'
import Reports from './pages/Reports.jsx'
import NotFound from './pages/NotFound.jsx'
import { RoleRoute } from './components/RoleRoute.jsx'
import { ProtectedRoute } from './components/ProtectedRoute.jsx'

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/login" replace />} />
      <Route path="/login" element={<Login />} />

      {/* Ruta genérica protegida para cualquier usuario autenticado */}
      <Route element={<ProtectedRoute />}>
        <Route path="/dashboard" element={<Dashboard />} />
      </Route>

      {/* Colaborador y Admin: gestionan pacientes, médicos y citas */}
      <Route element={<RoleRoute roles={['colaborador','admin']} />}>
        <Route path="/pacientes" element={<Patients />} />
        <Route path="/medicos" element={<Doctors />} />
      </Route>

      {/* Paciente: solo puede ver/crear sus propias citas (misma página de Citas por simplicidad) */}
      <Route element={<RoleRoute roles={['paciente', 'colaborador','admin']} />}>
        <Route path="/citas" element={<Appointments />} />
      </Route>

      {/* Admin: usuarios y reportes */}
      <Route element={<RoleRoute roles={['admin']} />}>
        <Route path="/usuarios" element={<Users />} />
        <Route path="/reportes" element={<Reports />} />
      </Route>

      <Route path="*" element={<NotFound />} />
    </Routes>
  )
}
