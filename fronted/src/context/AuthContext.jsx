import { createContext, useContext, useEffect, useState } from 'react'

const AuthContext = createContext(null)

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const raw = localStorage.getItem('auth_user')
    if (raw) setUser(JSON.parse(raw))
    setLoading(false)
  }, [])

  const login = (payload) => {
    setUser(payload)
    localStorage.setItem('auth_user', JSON.stringify(payload))
  }
  const logout = () => {
    setUser(null)
    localStorage.removeItem('auth_user')
  }

  const hasRole = (roles=[]) => {
    if (!user) return false
    if (!roles.length) return !!user
    return roles.includes(user.role)
  }

  return (
    <AuthContext.Provider value={{ user, login, logout, loading, hasRole }}>
      {children}
    </AuthContext.Provider>
  )
}

export function useAuth() {
  const ctx = useContext(AuthContext)
  if (!ctx) throw new Error('useAuth must be used within AuthProvider')
  return ctx
}
