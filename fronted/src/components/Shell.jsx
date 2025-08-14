import { Link, NavLink } from 'react-router-dom'
import { useAuth } from '../context/AuthContext.jsx'

export function Layout({ children }) {
  const { logout, user } = useAuth()
  const role = user?.role

  return (
    <div className="min-h-screen grid grid-cols-12">
      <aside className="col-span-12 md:col-span-3 lg:col-span-2 bg-white border-r">
        <div className="p-4 border-b flex items-center justify-between">
          <Link to="/dashboard" className="font-semibold text-lg">Citas Médicas</Link>
          <span className="text-xs text-gray-500 capitalize">{role}</span>
        </div>
        <nav className="p-4 space-y-2">
          <NavLink to="/dashboard" className={({isActive}) => isActive ? 'block bg-gray-100 rounded-md px-3 py-2' : 'block hover:bg-gray-50 rounded-md px-3 py-2'}>Dashboard</NavLink>

          {(role === 'admin' || role === 'colaborador') && (
            <>
              <NavLink to="/pacientes" className={({isActive}) => isActive ? 'block bg-gray-100 rounded-md px-3 py-2' : 'block hover:bg-gray-50 rounded-md px-3 py-2'}>Pacientes</NavLink>
              <NavLink to="/medicos" className={({isActive}) => isActive ? 'block bg-gray-100 rounded-md px-3 py-2' : 'block hover:bg-gray-50 rounded-md px-3 py-2'}>Médicos</NavLink>
              <NavLink to="/citas" className={({isActive}) => isActive ? 'block bg-gray-100 rounded-md px-3 py-2' : 'block hover:bg-gray-50 rounded-md px-3 py-2'}>Citas</NavLink>
            </>
          )}

          {role === 'paciente' && (
            <NavLink to="/citas" className={({isActive}) => isActive ? 'block bg-gray-100 rounded-md px-3 py-2' : 'block hover:bg-gray-50 rounded-md px-3 py-2'}>Mis Citas</NavLink>
          )}

          {role === 'admin' && (
            <>
              <NavLink to="/usuarios" className={({isActive}) => isActive ? 'block bg-gray-100 rounded-md px-3 py-2' : 'block hover:bg-gray-50 rounded-md px-3 py-2'}>Usuarios</NavLink>
              <NavLink to="/reportes" className={({isActive}) => isActive ? 'block bg-gray-100 rounded-md px-3 py-2' : 'block hover:bg-gray-50 rounded-md px-3 py-2'}>Reportes</NavLink>
            </>
          )}
        </nav>
        <div className="p-4 border-t">
          <button onClick={logout} className="btn btn-outline w-full">Cerrar sesión</button>
        </div>
      </aside>
      <main className="col-span-12 md:col-span-9 lg:col-span-10 p-6">
        {children}
      </main>
    </div>
  )
}
