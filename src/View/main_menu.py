import tkinter as tk
from tkinter import messagebox
from src.Model.sueldo_calculo import calcular_sueldo_neto
from src.Model.database import Sueldo, session  # Importa la clase Sueldo y la sesión de SQLAlchemy

def calcular_sueldo():
    try:
        # Obtener los valores de entrada
        nombre_trabajador_val = nombre_trabajador.get()
        sueldo_basico_val = float(sueldo_basico.get())
        dias_falta_val = int(dias_falta.get())
        minutos_tardanza_val = int(minutos_tardanza.get())
        horas_extras_val = float(horas_extras.get())

        # Llamada a la función de cálculo del sueldo
        sueldo_neto = calcular_sueldo_neto(sueldo_basico_val, dias_falta_val, minutos_tardanza_val, horas_extras_val)
        # Crear una nueva instancia de Sueldo
        sueldo_registrado = Sueldo(
            nombre_trabajador=nombre_trabajador_val,
            sueldo_basico=sueldo_basico_val,
            dias_falta=dias_falta_val,
            minutos_tardanza=minutos_tardanza_val,
            horas_extras=horas_extras_val,
            sueldo_neto=sueldo_neto
        )
        # Añadir el registro a la sesión y guardar en la base de datos
        session.add(sueldo_registrado)
        session.commit()
        # Actualizar el label con el resultado
        resultado_label.config(text=f"Sueldo Neto a pagar: {sueldo_neto:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores válidos.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Cálculo de Sueldo - Horizonte")
root.geometry("400x400")  # Aumentamos el tamaño de la ventana

# Configuración de la grilla
root.grid_columnconfigure(1, weight=1)

# Campos de entrada y etiquetas
tk.Label(root, text="Nombre del Trabajador:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
nombre_trabajador = tk.Entry(root)
nombre_trabajador.grid(row=0, column=1, padx=10, pady=10, sticky="we")

tk.Label(root, text="Sueldo Básico:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
sueldo_basico = tk.Entry(root)
sueldo_basico.grid(row=1, column=1, padx=10, pady=10, sticky="we")

tk.Label(root, text="Días de Faltas:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
dias_falta = tk.Entry(root)
dias_falta.grid(row=2, column=1, padx=10, pady=10, sticky="we")

tk.Label(root, text="Minutos de Tardanza:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
minutos_tardanza = tk.Entry(root)
minutos_tardanza.grid(row=3, column=1, padx=10, pady=10, sticky="we")

tk.Label(root, text="Horas Extras:").grid(row=4, column=0, padx=10, pady=10, sticky="e")
horas_extras = tk.Entry(root)
horas_extras.grid(row=4, column=1, padx=10, pady=10, sticky="we")

# Botón para calcular
boton_calcular = tk.Button(root, text="Calcular Sueldo", command=calcular_sueldo)
boton_calcular.grid(row=5, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

# Label para mostrar el resultado
resultado_label = tk.Label(root, text="Sueldo Neto a pagar: ")
resultado_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Iniciar la GUI
root.mainloop()
