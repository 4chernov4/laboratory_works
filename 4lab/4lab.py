import numpy as np
import matplotlib.pyplot as plt

xcoordinate = float(input("Введите координату x: "))
ycoordinate = float(input("Введите координату y: "))


def f(x):
    return x ** 2 + 2 * x - 10


def df(x):
    return -x ** 2 + 2 * x + 8


def gf(x):
    return 2 * x + 4


plt.axis([-10, 10, -100, 75])
plt.title('3 графика и точка ', fontsize=20, fontname='Times New Roman')
plt.xlabel('Ось х ', color='gray')
plt.ylabel('Ось у ', color='gray')
plt.grid(True)
xvalue = np.linspace(-10, 10, 10)
fig, ax = plt.subplots()
plt.plot(xcoordinate, ycoordinate, 'ro')
plt.plot(xvalue, f(xvalue), 'o-g', label='$x^2+2x-10$')
plt.plot(xvalue, df(xvalue), 'o-b', label='$-x^2+2x+8$')
plt.plot(xvalue, gf(xvalue), 'o-m', label='$2x+4$')
plt.legend()
ax.fill_between(xvalue, f(xvalue), df(xvalue), where=y2 > y1, interpolate=True,
                color='green', alpha=0.3)
ax.fill_between(x, y2, y3, where=y2 > y3, interpolate=True,
                color='yellow', alpha=0.2)
ax.fill_between(x, y3, y1, where=y3 > y1, interpolate=True,
                color='blue', alpha=0.2)
plt.show()
