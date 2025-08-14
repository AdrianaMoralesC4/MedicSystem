export default function DataTable({ columns = [], data = [], onEdit, onDelete }) {
  return (
    <div className="card p-4">
      <div className="overflow-auto">
        <table className="table">
          <thead>
            <tr>
              {columns.map(c => <th key={c.accessor} className="th px-3 py-2">{c.header}</th>)}
              {(onEdit || onDelete) && <th className="th px-3 py-2">Acciones</th>}
            </tr>
          </thead>
          <tbody>
            {data.map((row, idx) => (
              <tr key={idx}>
                {columns.map(c => <td key={c.accessor} className="td px-3">{row[c.accessor]}</td>)}
                {(onEdit || onDelete) && (
                  <td className="td px-3 space-x-2">
                    {onEdit && <button className="btn btn-outline" onClick={() => onEdit(row)}>Editar</button>}
                    {onDelete && <button className="btn btn-outline" onClick={() => onDelete(row)}>Eliminar</button>}
                  </td>
                )}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}
