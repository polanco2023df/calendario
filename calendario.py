from datetime import datetime, timedelta

# Estructura de datos para las reservas
reservas = {}

# Función para agregar una reserva
def agregar_reserva(nombre, fecha, hora):
    formato = "%Y-%m-%d %H:%M"
    inicio_reserva = datetime.strptime(f"{fecha} {hora}", formato)
    fin_reserva = inicio_reserva + timedelta(hours=1)
    
    for reserva in reservas.values():
        if reserva['inicio'] < fin_reserva and inicio_reserva < reserva['fin']:
            return f"Error: Ya hay una reserva para ese horario ({fecha} {hora})"
    
    reservas[nombre] = {'inicio': inicio_reserva, 'fin': fin_reserva}
    return f"Reserva realizada para {nombre} el {fecha} a las {hora}."

# Función para mostrar las reservas
def mostrar_reservas():
    for nombre, tiempo in reservas.items():
        print(f"{nombre}: {tiempo['inicio']} - {tiempo['fin']}")

# Ejemplo de uso
nombre = "Carlos Polanco"
fecha = "2024-07-20"
hora = "15:40"

print(agregar_reserva(nombre, fecha, hora))
mostrar_reservas()

# Intentar una reserva en un horario conflictivo
nombre2 = "Ana Lopez"
hora_conflictiva = "15:50"

print(agregar_reserva(nombre2, fecha, hora_conflictiva))
mostrar_reservas()

# Intentar una reserva en un horario no conflictivo
hora_no_conflictiva = "16:50"

print(agregar_reserva(nombre2, fecha, hora_no_conflictiva))
mostrar_reservas()
