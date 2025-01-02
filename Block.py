
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
# Sample Data for Strike Prices, Time to Maturity, and Implied 
#Volatility
strikes = np.linspace(80, 120, 10) # Strike prices
maturities = np.linspace(0.1, 2, 10) # Time to maturity (in years)
# Creating an artificial volatility surface
vol_surface = np.array([[0.2 + 0.05 * np.sin(strike) * np.exp(-maturity / 2)
for strike in strikes] for maturity in maturities])
# Plotting the Volatility Surface
X, Y = np.meshgrid(strikes, maturities)
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, vol_surface, cmap=cm.viridis, 
edgecolor='k')
# Labels and Title
ax.set_title("Implied Volatility Surface")
ax.set_xlabel("Strike Price")
ax.set_ylabel("Time to Maturity (Years)")
ax.set_zlabel("Implied Volatility")
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()