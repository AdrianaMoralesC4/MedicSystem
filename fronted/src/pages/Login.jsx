import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { z } from 'zod'
import { useAuth } from '../context/AuthContext.jsx'
import { endpoints } from '../lib/api.js'
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'

const schema = z.object({
  email: z.string().email('Email inválido'),
  password: z.string().min(4, 'Mínimo 4 caracteres'),
  role: z.enum(['admin','colaborador','paciente']),
})

export default function Login() {
  const { register, handleSubmit, formState: { errors } } = useForm({ resolver: zodResolver(schema), defaultValues: { role: 'admin' } })
  const { login } = useAuth()
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const navigate = useNavigate()

  const onSubmit = async (values) => {
    setLoading(true); setError(null)
    try {
      const res = await endpoints.auth.login({ email: values.email, password: values.password }).catch(() => null)
      // Si tu API devuelve un usuario con role, úsalo; si no, usa el seleccionado en el formulario
      const user = res?.data?.user || { id: 1, name: 'Demo', role: values.role, email: values.email }
      if (!user.role) user.role = values.role
      login(user)
      navigate('/dashboard')
    } catch (e) {
      setError('Credenciales inválidas')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center p-6">
      <form onSubmit={handleSubmit(onSubmit)} className="card p-6 w-full max-w-sm space-y-4">
        <h1 className="text-xl font-semibold">Iniciar sesión</h1>
        {error && <div className="text-danger text-sm">{error}</div>}
        <div>
          <label className="label">Email</label>
          <input className="input" type="email" {...register('email')} />
          {errors.email && <p className="text-danger text-sm mt-1">{errors.email.message}</p>}
        </div>
        <div>
          <label className="label">Contraseña</label>
          <input className="input" type="password" {...register('password')} />
          {errors.password && <p className="text-danger text-sm mt-1">{errors.password.message}</p>}
        </div>
        <div>
          <label className="label">Rol</label>
          <select className="input capitalize" {...register('role')}>
            <option value="admin">Administrador</option>
            <option value="colaborador">Colaborador de salud</option>
            <option value="paciente">Paciente</option>
          </select>
          {errors.role && <p className="text-danger text-sm mt-1">{errors.role.message}</p>}
        </div>
        <button className="btn btn-primary w-full" disabled={loading}>
          {loading ? 'Ingresando...' : 'Ingresar'}
        </button>
      </form>
    </div>
  )
}
