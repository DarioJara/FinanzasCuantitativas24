import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import streamlit as st

# Título de la aplicación
st.title("Volatility Surface Visualizer")

# Inputs interactivos para los parámetros
base_volatility = st.slider("Nivel base de volatilidad (Base Volatility)", min_value=0.1, max_value=1.0, value=0.2, step=0.01)
oscillation_factor = st.slider("Factor de oscilación (Oscillation Factor)", min_value=0.01, max_value=0.2, value=0.05, step=0.01)

# Generar datos para el rango de Strike Prices y Time to Maturity
strikes = np.linspace(80, 120, 10)  # Precios de ejercicio
maturities = np.linspace(0.1, 2, 10)  # Tiempo hasta el vencimiento (en años)

# Crear la superficie de volatilidad artificial
vol_surface = np.array([
    [
        base_volatility + oscillation_factor * np.sin(strike/10) * np.exp(-maturity / 2)
        for strike in strikes
    ]
    for maturity in maturities
])

# Crear el gráfico en 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Preparar datos para el gráfico
X, Y = np.meshgrid(strikes, maturities)
surf = ax.plot_surface(X, Y, vol_surface, cmap=cm.viridis, edgecolor='k')

# Etiquetas y título
ax.set_title("Implied Volatility Surface")
ax.set_xlabel("Strike Price")
ax.set_ylabel("Time to Maturity (Years)")
ax.set_zlabel("Implied Volatility")
fig.colorbar(surf, shrink=0.5, aspect=5)

# Mostrar el gráfico en Streamlit
st.pyplot(fig)