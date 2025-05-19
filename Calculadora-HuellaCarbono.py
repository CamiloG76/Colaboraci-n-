import tkinter as tk
from tkinter import messagebox
import os

factores = [0.233, 0.21, 0.271, 2.5, 0.4, 14.0, 0.9]  # Factor de emisión
actividades = [0] * 7  # Valores ingresados por el usuario
resultados = [0] * 7   # Resultados por categoría
colores_categoria = [["Electricidad", "#A2D2FF"], ["Transporte", "#BDE0FE"]]
impacto_categoria = [[0, 0] for _ in range(7)]  # Valor anterior y actual
mensaje_por_categoria = [["Electricidad", "Reduce el consumo usando bombillos LED."],
                          ["Carne", "Opta por comidas vegetarianas algunos días."],
                          ["Residuos", "Recicla y reutiliza siempre que puedas."]]

categorias = [
    "Electricidad consumida (kWh/mes)",
    "Kilómetros en transporte público (km/mes)",
    "Kilómetros en automóvil (km/mes)",
    "Carne consumida (kg/mes)",
    "Vegetales consumidos (kg/mes)",
    "Ropa comprada (unidades/mes)",
    "Residuos generados (kg/mes)"
]

def obtener_actividad(i):
    return float(entradas[i].get())

def calcular_emision(i, actividad):
    return actividad * factores[i]

def formatear_resultado(i):
    return f"{resultados[i]:.2f} kg CO₂"

def obtener_analisis(total):
    if total < 100:
        return "Tu huella es bastante baja. ¡Sigue así!"
    elif total < 300:
        return "Huella moderada. Puedes reducir el uso del automóvil y el consumo de carne."
    else:
        return "Huella alta. Considera usar transporte público, reducir carne y reciclar más."

def calcular_compensaciones(total):
    arboles = total / 21
    reciclaje = total / 1.5
    return arboles, reciclaje

def mostrar_resultados(total, analisis, arboles, reciclaje):
    resultado_var.set(f"🌍 Huella total estimada: {total:.2f} kg CO₂ / mes")
    analisis_final = (
        f"{analisis}\n\n"
        f"🌳 Árboles necesarios para compensar: {arboles:.1f} (anualmente)\n"
        f"♻️ Reciclaje mensual necesario: {reciclaje:.1f} kg"
    )
    analisis_var.set(analisis_final)
    guardar_resultado(nombre_entry.get(), correo_entry.get(), total, analisis_final)

def calcular():
    try:
        total = 0
        for i in range(len(categorias)):
            actividad = obtener_actividad(i)
            actividades[i] = actividad
            resultado = calcular_emision(i, actividad)
            impacto_categoria[i][0] = impacto_categoria[i][1]  # anterior
            impacto_categoria[i][1] = resultado  # actual
            resultados[i] = resultado
            total += resultado
            resultado_categorias[i].set(formatear_resultado(i))

        analisis = obtener_analisis(total)
        arboles, reciclaje = calcular_compensaciones(total)
        mostrar_resultados(total, analisis, arboles, reciclaje)

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa solo números válidos.")

def limpiar_gui():
    for entrada in entradas:
        entrada.delete(0, tk.END)
    for var in resultado_categorias:
        var.set("")
    resultado_var.set("")
    analisis_var.set("")

def reiniciar():
    nombre_entry.delete(0, tk.END)
    correo_entry.delete(0, tk.END)
    limpiar_gui()

def crear_archivo(path, texto):
    with open(path, "w", encoding="utf-8") as archivo:
        archivo.write(texto)

def guardar_resultado(nombre, correo, total, analisis):
    try:
        directorio = os.path.expanduser("~/Documentos")
        os.makedirs(directorio, exist_ok=True)
        archivo_path = os.path.join(directorio, "huella_carbono.txt")
        texto = f"Cálculo de Huella de Carbono\nNombre: {nombre}\nCorreo: {correo}\n\n"
        for i in range(len(categorias)):
            texto += f"{categorias[i]}: {actividades[i]} -> {resultados[i]:.2f} kg CO₂\n"
        texto += f"\nHuella total: {total:.2f} kg CO₂\n\nAnálisis:\n{analisis}\n"
        crear_archivo(archivo_path, texto)
        messagebox.showinfo("Guardado", f"Resultado guardado correctamente en:\n{archivo_path}")
    except:
        messagebox.showerror("Error", "No se pudo guardar el archivo.")

# Interfaz grafica