import sqlite3

# Crea la DB
conexion = sqlite3.connect("students_database.db")

# Crea el cursor para interactuar con la DB
cursor = conexion.cursor()

# Crea la tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS estudiantes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    correo TEXT NOT NULL
)
""")


# Ingresa valores a la tabla
cursor.execute("INSERT INTO estudiantes (nombre, correo) VALUES ('Juan Pérez', 'juanperez@ejemplo.com')")
cursor.execute("INSERT INTO estudiantes (nombre, correo) VALUES ('Eduardo Peña', 'edu.peña@ejemplo.com')")

# Confirma los cambios a la tabla
conexion.commit()

# Consulta los registros totales de la tabla
cursor.execute("SELECT * FROM estudiantes")

# Obtener los resultados de la Consulta
estudiantes = cursor.fetchall()

# Mostrar los resultados
print("\n[Estudiantes]\n")
for estudiante in estudiantes:
    print(f"ID: {estudiante[0]}, Nombre: {estudiante[1]}, Correo: {estudiante[2]},")

cursor.close()
conexion.close()

