import { useEffect, useState } from 'react'
import DataTable from '../components/DataTable.jsx'
import { endpoints } from '../lib/api.js'
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { pacienteSchema } from '../lib/validators.js'

export default function Patients() {
  const [data, setData] = useState([])
  const [editing, setEditing] = useState(null)
  const { register, handleSubmit, reset, formState: { errors } } = useForm({ resolver: zodResolver(pacienteSchema) })

  const fetchData = async () => {
    try {
      const res = await endpoints.pacientes.list()
      setData(res.data || [])
    } catch {
      // demo fallback
      setData([
        { id: '1', identificacion: '1712345678', nombres: 'Ana', apellidos: 'Pérez', telefono: '0999999999' },
      ])
    }
  }

  useEffect(() => { fetchData() }, [])

  const onSubmit = async (values) => {
    if (editing) {
      await endpoints.pacientes.update(editing.id, values).catch(()=>{})
    } else {
      await endpoints.pacientes.create(values).catch(()=>{})
    }
    reset(); setEditing(null); fetchData()
  }

  const onEdit = (row) => { setEditing(row); reset(row) }
  const onDelete = async (row) => { await endpoints.pacientes.remove(row.id).catch(()=>{}); fetchData() }

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-semibold">Pacientes</h1>
      <form onSubmit={handleSubmit(onSubmit)} className="card p-4 grid md:grid-cols-2 gap-4">
        <div><label className="label">Identificación</label><input className="input" {...register('identificacion')} />{errors.identificacion && <p className="text-danger text-sm">{errors.identificacion.message}</p>}</div>
        <div><label className="label">Nombres</label><input className="input" {...register('nombres')} />{errors.nombres && <p className="text-danger text-sm">{errors.nombres.message}</p>}</div>
        <div><label className="label">Apellidos</label><input className="input" {...register('apellidos')} />{errors.apellidos && <p className="text-danger text-sm">{errors.apellidos.message}</p>}</div>
        <div><label className="label">Teléfono</label><input className="input" {...register('telefono')} /></div>
        <div><label className="label">Email</label><input className="input" type="email" {...register('email')} /></div>
        <div className="md:col-span-2">
          <button className="btn btn-primary">{editing ? 'Actualizar' : 'Agregar'}</button>
          {editing && <button type="button" className="btn btn-outline ml-2" onClick={()=>{reset(); setEditing(null)}}>Cancelar</button>}
        </div>
      </form>

      <DataTable
        columns={[
          { header: 'ID', accessor: 'id' },
          { header: 'Identificación', accessor: 'identificacion' },
          { header: 'Nombres', accessor: 'nombres' },
          { header: 'Apellidos', accessor: 'apellidos' },
          { header: 'Teléfono', accessor: 'telefono' },
        ]}
        data={data}
        onEdit={onEdit}
        onDelete={onDelete}
      />
    </div>
  )
}
