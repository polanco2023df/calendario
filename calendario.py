import streamlit as st
import pandas as pd
import datetime

# Título de la aplicación
st.title("Reservación de Citas para Pacientes")

# Crear el DataFrame para almacenar las reservaciones
if 'reservations' not in st.session_state:
    st.session_state['reservations'] = pd.DataFrame(columns=['Paciente', 'Fecha', 'Hora'])

# Función para agregar una nueva reservación
def add_reservation(paciente, fecha, hora):
    new_reservation = pd.DataFrame([[paciente, fecha, hora]], columns=['Paciente', 'Fecha', 'Hora'])
    st.session_state['reservations'] = pd.concat([st.session_state['reservations'], new_reservation], ignore_index=True)

# Formulario para agregar una nueva reservación
st.header("Agregar Nueva Reservación")
paciente = st.text_input("Nombre del Paciente")
fecha = st.date_input("Fecha", datetime.date.today())
hora = st.time_input("Hora", datetime.datetime.now().time())

if st.button("Reservar"):
    # Verificar si ya existe una reservación para el mismo paciente en el mismo horario
    existing_reservation = st.session_state['reservations'][
        (st.session_state['reservations']['Paciente'] == paciente) &
        (st.session_state['reservations']['Fecha'] == str(fecha)) &
        (st.session_state['reservations']['Hora'] == str(hora))
    ]
    
    if existing_reservation.empty:
        add_reservation(paciente, fecha, hora)
        st.success("Reservación agregada exitosamente")
    else:
        st.error("El paciente ya tiene una reservación en ese horario")

# Mostrar todas las reservaciones
st.header("Reservaciones Existentes")
st.dataframe(st.session_state['reservations'])

