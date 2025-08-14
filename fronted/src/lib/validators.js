import { z } from 'zod'

export const pacienteSchema = z.object({
  identificacion: z.string().min(5, 'Identificación requerida'),
  nombres: z.string().min(2, 'Nombre requerido'),
  apellidos: z.string().min(2, 'Apellido requerido'),
  telefono: z.string().optional(),
  email: z.string().email('Email inválido').optional(),
})

export const medicoSchema = z.object({
  nombres: z.string().min(2, 'Nombre requerido'),
  apellidos: z.string().min(2, 'Apellido requerido'),
  especialidad: z.string().min(2, 'Especialidad requerida'),
})

export const citaSchema = z.object({
  pacienteId: z.string().min(1, 'Paciente requerido'),
  medicoId: z.string().min(1, 'Médico requerido'),
  fecha: z.string().min(1, 'Fecha requerida'),
  hora: z.string().min(1, 'Hora requerida'),
  motivo: z.string().min(3, 'Motivo requerido'),
})
