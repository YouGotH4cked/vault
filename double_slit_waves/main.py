import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ==========================================
# 1. SLIT CLASS
# ==========================================
class WaveSource:
    def __init__(self, x0, y0, amplitude=1.0, k=2.5, omega=4.0):
        self.x0 = x0          # Poziția fantei pe axa X
        self.y0 = y0          # Poziția fantei pe axa Y
        self.A = amplitude    # Amplitudinea valului
        self.k = k            # Numărul de undă (desimea spațială)
        self.omega = omega    # Frecvența (viteza în timp)

    def get_wave(self, X, Y, t):
        # Distanța de la fantă la fiecare punct (X, Y) din grilă
        r = np.sqrt((X - self.x0)**2 + (Y - self.y0)**2)
        r = np.maximum(r, 1e-5)  # Evităm împărțirea la zero

        # Formula lui Euler sub formă complexă: A * e^(i * (k*r - omega*t)) / sqrt(r)
        faza = self.k * r - self.omega * t
        return (self.A / np.sqrt(r)) * np.exp(1j * faza)


# ==========================================
# 2. SLITS SETUP
# ==========================================
x = np.linspace(0, 10, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

slit_1 = WaveSource(x0=0, y0=-1.5)
slit_2 = WaveSource(x0=0, y0=1.5)
slits = [slit_1, slit_2]


# ==========================================
# 3. GRAPH SETUP
# ==========================================
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Cadru inițial (la t = 0)
Z_total_0 = sum(f.get_wave(X, Y, t=0) for f in slits)
surf = [ax.plot_surface(X, Y, Z_total_0.real, cmap='ocean', vmin=-1.0, vmax=1.0)]

ax.set_zlim(-2, 2)
ax.set_title('3D Simulation - Double slit experiment')


# ==========================================
# 4. ANIMATION FUNCTION
# ==========================================
def update(frame):
    t = frame * 0.05  # Timpul avansează cu 0.05s la fiecare cadru

    # Adunăm undele complexe generate de cele două fante
    Z_total = sum(f.get_wave(X, Y, t) for f in slits)

    # Ștergem vechea suprafață și desenăm noua suprafață folosind doar PARTEA REALĂ
    surf[0].remove()
    surf[0] = ax.plot_surface(X, Y, Z_total.real, cmap='ocean', vmin=-1.0, vmax=1.0, antialiased=False)
    return surf

# Run the animation
anim = FuncAnimation(fig, update, frames=200, interval=30, blit=False)
plt.show()