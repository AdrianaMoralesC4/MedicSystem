export default function Users() {
  // Esta página sería para admins: gestión de usuarios y asignación de roles
  // En producción, esto se conectaría a /usuarios (listar/crear/actualizar/bloquear)
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-semibold">Usuarios</h1>
      <div className="card p-4">
        <p className="text-sm text-gray-600">Desde aquí el administrador puede crear usuarios y asignar roles (admin, colaborador, paciente).</p>
      </div>
    </div>
  )
}
