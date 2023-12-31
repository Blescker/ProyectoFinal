import tkinter as tk #Biblioteca para la interfaz
from tkinter import messagebox #Para mostrar los mensajes de error

#Modulos importados
from src.Model.sueldo_calculo import calcular_sueldo_neto 
from src.Model.database import Sueldo, session  # Importa la clase Sueldo y la sesión de SQLAlchemy

#Biblioteca para generar los pdf
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def generar_boleta(nombre, sueldo_basico, dias_falta, minutos_tardanza, horas_extras, sueldo_neto): #Argumentos que recibe
    c = canvas.Canvas(f"boleta_{nombre}.pdf", pagesize=letter) #Nombre de la boleta  y tamaño de pagina
    c.drawString(100, 750, f"Boleta de Pago para {nombre}")
    c.drawString(100, 730, f"Sueldo Básico: {sueldo_basico}")
    c.drawString(100, 710, f"Días de Faltas: {dias_falta}")
    c.drawString(100, 690, f"Minutos de Tardanza: {minutos_tardanza}")
    c.drawString(100, 670, f"Horas Extras: {horas_extras}")
    c.drawString(100, 650, f"Sueldo Neto: {sueldo_neto:.2f}")

    c.save()
    
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
        #Generar la boleta
        generar_boleta(nombre_trabajador.get(), sueldo_basico_val, dias_falta_val, minutos_tardanza_val, horas_extras_val, sueldo_neto)
        # Añadir el registro a la sesión y guardar en la base de datos
        session.add(sueldo_registrado)
        #Guardar cambios
        session.commit()
        # Actualizar el label con el resultado
        resultado_label.config(text=f"Sueldo Neto a pagar: {sueldo_neto:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores válidos.")

def mostrar_reportes():
    #Crea una nueva ventana, venta_reportes nombre de la variable de la ventana
    ventana_reportes = tk.Toplevel(root)
    ventana_reportes.title("Reportes de Sueldos")
    ventana_reportes.geometry("400x400")

    # Consultar la base de datos para obtener los sueldos
    sueldos = session.query(Sueldo).all()
    for i, registro in enumerate(sueldos):
        tk.Label(ventana_reportes, text=f"{registro.nombre_trabajador}: {registro.sueldo_neto:.2f} soles").grid(row=i, column=0, sticky="w")
        
# Configuración de la ventana principal
root = tk.Tk()
root.title("Cálculo de Sueldo - Horizonte")
root.geometry("400x400")  # Aumentamos el tamaño de la ventana
# Configuración del tamaño
root.grid_columnconfigure(1, weight=1)
# Campos de entrada y etiquetas
tk.Label(root, text="Nombre del Trabajador:").grid(row=0, column=0, padx=10, pady=10, sticky="e") #label nombre stick=e alinear derecha
nombre_trabajador = tk.Entry(root) #Para ingresar los datos
nombre_trabajador.grid(row=0, column=1, padx=10, pady=10, sticky="we") #oeste y este west east, crecera en esta direccion

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
boton_calcular = tk.Button(root, text="Calcular Sueldo", command=calcular_sueldo) # Crear boton calcular
boton_calcular.grid(row=5, column=0, columnspan=2, padx=20, pady=20, sticky="ew") #

# Label para mostrar el resultado
resultado_label = tk.Label(root, text="Sueldo Neto a pagar: ")
resultado_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Botón para ver reportes de sueldos
boton_ver_reportes = tk.Button(root, text="Ver Reportes de Sueldos", command=mostrar_reportes)
boton_ver_reportes.grid(row=8, column=1, padx=10, pady=10, sticky="e")
# Iniciar la GUI
root.mainloop()