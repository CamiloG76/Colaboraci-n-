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

