import { useEffect, useState } from 'react'
import DataTable from '../components/DataTable.jsx'
import { endpoints } from '../lib/api.js'
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { citaSchema } from '../lib/validators.js'

export default function Appointments() {
  const [data, setData] = useState([])
  const [editing, setEditing] = useState(null)
  const [pacientes, setPacientes] = useState([])
  const [medicos, setMedicos] = useState([])

  const { register, handleSubmit, reset, formState: { errors } } = useForm({ resolver: zodResolver(citaSchema) })

  const fetchAll = async () => {
    try {
      const [citasRes, pacRes, medRes] = await Promise.all([
        endpoints.citas.list(), endpoints.pacientes.list(), endpoints.medicos.list()
      ])
      setData(citasRes.data || [])
      setPacientes(pacRes.data || [])
      setMedicos(medRes.data || [])
    } catch {
      // Demo fallback
      setPacientes([{ id: '1', nombres: 'Ana', apellidos: 'Pérez' }])
      setMedicos([{ id: '1', nombres: 'Luis', apellidos: 'García' }])
      setData([{ id: '1', pacienteId: '1', medicoId: '1', fecha: '2025-08-15', hora: '09:00', motivo: 'Chequeo general' }])
    }
  }

  useEffect(() => { fetchAll() }, [])

  const onSubmit = async (values) => {
    if (editing) await endpoints.citas.update(editing.id, values).catch(()=>{})
    else await endpoints.citas.create(values).catch(()=>{})
    reset(); setEditing(null); fetchAll()
  }

  const onEdit = (row) => { setEditing(row); reset(row) }
  const onDelete = async (row) => { await endpoints.citas.remove(row.id).catch(()=>{}); fetchAll() }

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-semibold">Citas</h1>
      <form onSubmit={handleSubmit(onSubmit)} className="card p-4 grid md:grid-cols-3 gap-4">
        <div>
          <label className="label">Paciente</label>
          <select className="input" {...register('pacienteId', { required: true })}>
            <option value="">Seleccione...</option>
            {pacientes.map(p => <option key={p.id} value={p.id}>{p.nombres} {p.apellidos}</option>)}
          </select>
          {errors.pacienteId && <p className="text-danger text-sm">{errors.pacienteId.message}</p>}
        </div>
        <div>
          <label className="label">Médico</label>
          <select className="input" {...register('medicoId', { required: true })}>
            <option value="">Seleccione...</option>
            {medicos.map(m => <option key={m.id} value={m.id}>{m.nombres} {m.apellidos}</option>)}
          </select>
          {errors.medicoId && <p className="text-danger text-sm">{errors.medicoId.message}</p>}
        </div>
        <div>
          <label className="label">Fecha</label>
          <input className="input" type="date" {...register('fecha')} />
          {errors.fecha && <p className="text-danger text-sm">{errors.fecha.message}</p>}
        </div>
        <div>
          <label className="label">Hora</label>
          <input className="input" type="time" {...register('hora')} />
          {errors.hora && <p className="text-danger text-sm">{errors.hora.message}</p>}
        </div>
        <div className="md:col-span-3">
          <label className="label">Motivo</label>
          <input className="input" {...register('motivo')} />
          {errors.motivo && <p className="text-danger text-sm">{errors.motivo.message}</p>}
        </div>
        <div className="md:col-span-3">
          <button className="btn btn-primary">{editing ? 'Actualizar' : 'Crear cita'}</button>
          {editing && <button type="button" className="btn btn-outline ml-2" onClick={()=>{reset(); setEditing(null)}}>Cancelar</button>}
        </div>
      </form>

      <DataTable
        columns={[
          { header: 'ID', accessor: 'id' },
          { header: 'Paciente', accessor: 'pacienteId' },
          { header: 'Médico', accessor: 'medicoId' },
          { header: 'Fecha', accessor: 'fecha' },
          { header: 'Hora', accessor: 'hora' },
          { header: 'Motivo', accessor: 'motivo' },
        ]}
        data={data}
        onEdit={onEdit}
        onDelete={onDelete}
      />
    </div>
  )
}
