import { Navigate, Outlet } from 'react-router-dom'
import { useAuth } from '../context/AuthContext.jsx'
import { Layout } from './Shell.jsx'

export function RoleRoute({ roles = [] }) {
  const { user, loading, hasRole } = useAuth()
  if (loading) return <div className="p-6">Cargando...</div>
  if (!user) return <Navigate to="/login" replace />
  if (!hasRole(roles)) return <Navigate to="/dashboard" replace />
  return (
    <Layout>
      <Outlet />
    </Layout>
  )
}
