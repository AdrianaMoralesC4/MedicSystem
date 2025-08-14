# Sistema de Citas Médicas — React + Vite + Tailwind

Proyecto base para tu TFINAL. Incluye:
- Rutas protegidas (login requerido)
- Módulos: Pacientes, Médicos, Citas (CRUD básico)
- Cliente Axios y validación con zod + react-hook-form
- TailwindCSS listo
- Estructura pensada para entregar en repositorio y cumplir la rúbrica

## Requisitos
- Node.js (LTS) y npm

## Instalación
```bash
npm install
npm run dev
```

## Variables de entorno
Crea `.env` (opcional):
```
VITE_API_URL=http://localhost:3000/api
```

## Conecta tu API (Tarea 02.03)
Ajusta rutas en `src/lib/api.js` según tus endpoints reales.

## Rutas principales
- `/login` — acceso
- `/dashboard`
- `/pacientes`
- `/medicos`
- `/citas`

## Commits sugeridos (mín. 20)
1. init: scaffolding de proyecto
2. feat: configurar tailwind
3. feat: auth context y protected route
4. feat: páginas base (dashboard/pacientes/medicos/citas)
5. feat: tabla y formularios con validación
6. feat: cliente axios y variables de entorno
7. chore: agregar README y scripts
8. fix: validaciones de formularios
9. feat: CRUD pacientes
10. feat: CRUD medicos
11. feat: CRUD citas
12. feat: manejo de errores y estados de carga
13. ui: estilos de botones/inputs
14. ui: layout con sidebar
15. test: (opcional) hooks o utilidades
16. docs: agregar instrucciones de despliegue
17. refactor: separar componentes reutilizables
18. feat: filtros/búsqueda en tablas
19. feat: paginación (opcional)
20. release: versión candidata

## Tailwind
- Estilos utilitarios en `src/styles/index.css`

## Construcción
```bash
npm run build
npm run preview
```

> Recuerda subir tu repositorio (GitHub/GitLab) y el PDF con evidencias (pantallas, explicación técnica, y enlace al repo).


## Roles y permisos
- **admin**: todo (pacientes, médicos, citas, usuarios, reportes)
- **colaborador**: pacientes, médicos y citas
- **paciente**: solo citas propias (demo usa misma vista)

En `Login` puedes elegir el rol de prueba si tu API aún no devuelve el rol.
