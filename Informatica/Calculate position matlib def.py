import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
print("En este programa se calculará la posición de una partícula suponiendo un movimiento uniformemente acelerado")
#Crear gráfico
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(left=0.1, bottom=0.35)  #Ajustar sliders

#Función grafico
def grafica(x0, v0, a, t_total):
    t = np.linspace(0, t_total, 100)  #Intervalo de tiempo
    x = x0 + v0 * t + 0.5 * a * (t ** 2)  #Ecuación de posición de la partícula
    ax.clear()
    ax.plot(t, x, label="Posición de la partícula", color='b')
    ax.set_title('Movimiento de una partícula en movimiento uniformemente acelerado')
    ax.set_xlabel('Tiempo (s)')
    ax.set_ylabel('Posición (m)')
    ax.legend()
    ax.grid(True)

#Valores iniciales
x0_init = 0
v0_init = 0
a_init = 0
t_total_init = 10
grafica(x0_init, v0_init, a_init, t_total_init)

#Sliders para cada parámetro
ax_x0 = plt.axes([0.25, 0.25, 0.5, 0.01], facecolor='blue')
ax_v0 = plt.axes([0.25, 0.2, 0.5, 0.01], facecolor='blue')
ax_a = plt.axes([0.25, 0.15, 0.5, 0.01], facecolor='blue')
ax_t_total = plt.axes([0.25, 0.1, 0.5, 0.01], facecolor='blue')

slider_x0 = Slider(ax_x0, 'Posición Inicial (m)', 0.0, 1000000000000000000000000000.0, valinit=x0_init)
slider_v0 = Slider(ax_v0, 'Velocidad Inicial (m/s)', -1000000000000000000000000000.0, 1000000000000000000000000000.0, valinit=v0_init)
slider_a = Slider(ax_a, 'Aceleración (m/s^2)', -1000000000000000000000000000.0, 1000000000000000000000000000.0, valinit=a_init)
slider_t_total = Slider(ax_t_total, 'Tiempo (s)', 0.0, 500.0, valinit=t_total_init)

#Actualización gráfica
def actualizar(val):
    grafica(slider_x0.val, slider_v0.val, slider_a.val, slider_t_total.val)
slider_x0.on_changed(actualizar)
slider_v0.on_changed(actualizar)
slider_a.on_changed(actualizar)
slider_t_total.on_changed(actualizar)

plt.show()
