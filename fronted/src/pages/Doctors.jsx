import { useEffect, useState } from 'react'
import DataTable from '../components/DataTable.jsx'
import { endpoints } from '../lib/api.js'
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { medicoSchema } from '../lib/validators.js'

export default function Doctors() {
  const [data, setData] = useState([])
  const [editing, setEditing] = useState(null)
  const { register, handleSubmit, reset, formState: { errors } } = useForm({ resolver: zodResolver(medicoSchema) })

  const fetchData = async () => {
    try {
      const res = await endpoints.medicos.list()
      setData(res.data || [])
    } catch {
      setData([
        { id: '1', nombres: 'Luis', apellidos: 'García', especialidad: 'Cardiología' },
      ])
    }
  }

  useEffect(() => { fetchData() }, [])

  const onSubmit = async (values) => {
    if (editing) await endpoints.medicos.update(editing.id, values).catch(()=>{})
    else await endpoints.medicos.create(values).catch(()=>{})
    reset(); setEditing(null); fetchData()
  }

  const onEdit = (row) => { setEditing(row); reset(row) }
  const onDelete = async (row) => { await endpoints.medicos.remove(row.id).catch(()=>{}); fetchData() }

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-semibold">Médicos</h1>
      <form onSubmit={handleSubmit(onSubmit)} className="card p-4 grid md:grid-cols-3 gap-4">
        <div><label className="label">Nombres</label><input className="input" {...register('nombres')} />{errors.nombres && <p className="text-danger text-sm">{errors.nombres.message}</p>}</div>
        <div><label className="label">Apellidos</label><input className="input" {...register('apellidos')} />{errors.apellidos && <p className="text-danger text-sm">{errors.apellidos.message}</p>}</div>
        <div><label className="label">Especialidad</label><input className="input" {...register('especialidad')} />{errors.especialidad && <p className="text-danger text-sm">{errors.especialidad.message}</p>}</div>
        <div className="md:col-span-3">
          <button className="btn btn-primary">{editing ? 'Actualizar' : 'Agregar'}</button>
          {editing && <button type="button" className="btn btn-outline ml-2" onClick={()=>{reset(); setEditing(null)}}>Cancelar</button>}
        </div>
      </form>

      <DataTable
        columns={[
          { header: 'ID', accessor: 'id' },
          { header: 'Nombres', accessor: 'nombres' },
          { header: 'Apellidos', accessor: 'apellidos' },
          { header: 'Especialidad', accessor: 'especialidad' },
        ]}
        data={data}
        onEdit={onEdit}
        onDelete={onDelete}
      />
    </div>
  )
}
