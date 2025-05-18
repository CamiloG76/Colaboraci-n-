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
