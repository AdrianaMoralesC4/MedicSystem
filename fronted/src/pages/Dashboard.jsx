export default function Dashboard() {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-semibold">Dashboard</h1>
      <div className="grid md:grid-cols-3 gap-4">
        <div className="card p-4">
          <div className="text-gray-500 text-sm">Citas de hoy</div>
          <div className="text-3xl font-bold">8</div>
        </div>
        <div className="card p-4">
          <div className="text-gray-500 text-sm">Pacientes activos</div>
          <div className="text-3xl font-bold">124</div>
        </div>
        <div className="card p-4">
          <div className="text-gray-500 text-sm">Médicos</div>
          <div className="text-3xl font-bold">12</div>
        </div>
      </div>
    </div>
  )
}
