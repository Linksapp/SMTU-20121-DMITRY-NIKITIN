from sympy import Symbol, cos, sin, lambdify
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

x = np.arange(0, 5, 0.01)
y1 = (2 * x**2 - 3 * x + 7) * np.cos((x**2 / 2) + 8)


j = Symbol('j')
y2 = ((2 * j**2 - 3 * j + 7) * cos((j**2 / 2) + 8)).diff(j)
print(f'Первая производная: {y2}')
y3 = y2.diff(j)
print(f'Вторая производная: {y3}')

def arc(g):
    return (1 + -g*(2*g**2 - 3*g + 7)*sin(g**2/2 + 8) + (4*g - 3)*cos(g**2/2 + 8)**2)**1/2
arclength, err = integrate.quad(arc, 0, 5)
print(f'Длина дуги: {arclength}')


fig, axs = plt.subplots(2, 2, figsize=(12, 7))
x0 = 2
fx0 = (2 * x0**2 - 3 * x0 + 7) * np.cos((x0**2 / 2) + 8)
fx0d = lambdify(j, y2)(x0)
yk = fx0 + fx0d * (x-x0)
yn = fx0 - (x-x0)/fx0d

for x0 in range(6):
    fx0 = (2 * x0**2 - 3 * x0 + 7) * np.cos((x0**2 / 2) + 8)
    fx0d = lambdify(j, y2)(x0)
    yk_k = fx0 + fx0d * (x-x0)
    axs[1, 1].plot(x, yk_k, '--')




axs[0, 0].plot(x, y1)
axs[0, 0].plot(x[list(y1).index(y1.max())], y1.max(), 'o', color='b')
axs[0, 0].plot(x[list(y1).index(y1.min())], y1.min(), 'o', color='b')
axs[0, 0].plot(x, yk, '--', color='r')
axs[0, 0].plot(x, yn, '--', color='g')
axs[0, 1].plot(x, lambdify(j, y2, 'numpy')(x), color='r')
axs[1, 0].plot(x, lambdify(j, y3, 'numpy')(x), color='g')
axs[1, 1].plot(x, y1)
axs[1, 1].set_ylim(-30, 40) 
plt.show()