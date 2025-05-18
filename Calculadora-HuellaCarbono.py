import tkinter as tk
from tkinter import messagebox
import os

# Matriz: [actividad, factor_emisión, resultado]
matriz = [
    [0, 0.233, 0],  # Electricidad (kWh)
    [0, 0.21, 0],   # Transporte público (km)
    [0, 0.271, 0],  # Automóvil (km)
    [0, 2.5, 0],    # Carne (kg)
    [0, 0.4, 0],    # Vegetales (kg)
    [0, 14.0, 0],   # Ropa (unidades)
    [0, 0.9, 0]     # Residuos (kg)
]

categorias = [
    "Electricidad consumida (kWh/mes)",
    "Kilómetros en transporte público (km/mes)",
    "Kilómetros en automóvil (km/mes)",
    "Carne consumida (kg/mes)",
    "Vegetales consumidos (kg/mes)",
    "Ropa comprada (unidades/mes)",
    "Residuos generados (kg/mes)"
]

def calcular():
    try:
        total = 0
        for i in range(len(matriz)):
            actividad = float(entradas[i].get())
            matriz[i][0] = actividad
            matriz[i][2] = actividad * matriz[i][1]
            total += matriz[i][2]
            resultado_categorias[i].set(f"{matriz[i][2]:.2f} kg CO₂")

        resultado_var.set(f"🌍 Huella total estimada: {total:.2f} kg CO₂ / mes")

        # Análisis del resultado
        if total < 100:
            analisis = "Tu huella es bastante baja. ¡Sigue así!"
        elif total < 300:
            analisis = "Huella moderada. Puedes reducir el uso del automóvil y el consumo de carne."
        else:
            analisis = "Huella alta. Considera usar transporte público, reducir carne y reciclar más."

        # Compensaciones
        arboles = total / 21  # 1 árbol ≈ 21 kg CO₂/año
        reciclaje = total / 1.5  # 1.5 kg CO₂ ahorrado por 1 kg reciclado

        analisis_final = (
            f"{analisis}\n\n"
            f"🌳 Árboles necesarios para compensar: {arboles:.1f} (anualmente)\n"
            f"♻️ Reciclaje mensual necesario: {reciclaje:.1f} kg"
        )
        analisis_var.set(analisis_final)

        guardar_resultado(nombre_entry.get(), correo_entry.get(), total, analisis_final)

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa solo números válidos.")

def reiniciar():
    nombre_entry.delete(0, tk.END)
    correo_entry.delete(0, tk.END)
    for entrada in entradas:
        entrada.delete(0, tk.END)
    for var in resultado_categorias:
        var.set("")
    resultado_var.set("")
    analisis_var.set("")
def guardar_resultado(nombre, correo, total, analisis):
    try:
        directorio = os.path.expanduser("~/Documentos")
        os.makedirs(directorio, exist_ok=True)
        archivo_path = os.path.join(directorio, "huella_carbono.txt")
        with open(archivo_path, "w", encoding="utf-8") as archivo:
            archivo.write("Cálculo de Huella de Carbono\n")
            archivo.write(f"Nombre: {nombre}\nCorreo: {correo}\n\n")
            for i in range(len(categorias)):
                archivo.write(f"{categorias[i]}: {matriz[i][0]} -> {matriz[i][2]:.2f} kg CO₂\n")
            archivo.write(f"\nHuella total: {total:.2f} kg CO₂\n")
            archivo.write(f"\nAnálisis:\n{analisis}\n")
        messagebox.showinfo("Guardado", f"Resultado guardado correctamente en:\n{archivo_path}")
    except:
        messagebox.showerror("Error", "No se pudo guardar el archivo.")

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Calculadora de Huella de Carbono")
ventana.configure(bg="#e6f2ff")
ventana.geometry("580x620")
ventana.resizable(False, False)