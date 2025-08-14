export default function Reports() {
  // Aquí puedes montar KPIs de citas, productividad por médico, etc.
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-semibold">Reportes</h1>
      <div className="grid md:grid-cols-3 gap-4">
        <div className="card p-4"><div className="text-gray-500 text-sm">Citas del mes</div><div className="text-3xl font-bold">132</div></div>
        <div className="card p-4"><div className="text-gray-500 text-sm">% de ausencias</div><div className="text-3xl font-bold">4.1%</div></div>
        <div className="card p-4"><div className="text-gray-500 text-sm">Promedio de espera</div><div className="text-3xl font-bold">12m</div></div>
      </div>
    </div>
  )
}
