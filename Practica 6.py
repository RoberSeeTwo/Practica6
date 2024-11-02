import numpy as np
import matplotlib.pyplot as plt
import random

def maxArea(height):
    n = len(height)
    max_area = 0
    left = 0
    right = n - 1
    max_left = left
    max_right = right
    
    while left < right:
        current_height = min(height[left], height[right])
        current_width = right - left
        current_area = current_height * current_width
        
        if current_area > max_area:
            max_area = current_area
            max_left = left
            max_right = right
            
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_area, max_left, max_right

def plot_water_container(height):
    # Calcular el área máxima y los índices de las barras límite
    max_area, left_idx, right_idx = maxArea(height)
    
    # Crear la figura y los ejes
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plotear todas las barras en gris claro
    x = range(len(height))
    plt.bar(x, height, color='black', alpha=1)
    
    # Resaltar las barras límite en rojo
    plt.bar(left_idx, height[left_idx], color='red', alpha=1)
    plt.bar(right_idx, height[right_idx], color='red', alpha=1)
    
    # Dibujar el agua contenida
    water_height = min(height[left_idx], height[right_idx])
    water_x = np.arange(left_idx, right_idx + 1)
    plt.fill_between(water_x, 0, water_height, color='blue', alpha=0.5)
    
    # Configurar el gráfico
    plt.title(f'Contenedor de Agua Máximo (Área: {max_area})')
    plt.xlabel('Posición')
    plt.ylabel('Altura')
    
    return plt

# Generar datos aleatorios similares al código C
n = random.randint(2, 100000)  # Usar menos barras para mejor visualización
height = [random.randint(0, 10000) for _ in range(n)]

# Crear y mostrar el gráfico
plot = plot_water_container(height)
plot.show()