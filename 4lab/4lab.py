import matplotlib.pyplot as plt
import numpy as np

xi = float(input('Введите х:'))
yi = float(input('Введите у:'))


def f1(x):
    return x ** 2 + x - 14


def f2(x):
    return -x ** 2 + 2 * x + 10


def f3(x):
    return 2 * x - 6


def check_point_in_area(x, y):
    if f1(x) <= y <= f2(x) and y >= f3(x):
        return True
    else:
        return False


print(check_point_in_area(xi, yi))


plt.axis([-10, 10, -20, 20])
plt.title('Лаба 1', fontsize=20, fontname='Times New Roman')
plt.xlabel('Ось x', color='gray')
plt.ylabel('Ось y', color='gray')
plt.ioff()
x = np.arange(-10, 10, 0.01)
y1 = x ** 2 + x - 14
y2 = -x ** 2 + 2 * x + 10
y3 = 2 * x - 6


dn = np.maximum(y1, y3)

plt.plot(x, y1, 'r', x, y2, 'b', x, y3, 'g', linestyle='solid')
plt.fill_between(x, dn, y2, where=dn < y2, interpolate=True,
                color='green', alpha=0.3)

plt.plot(xi, yi, "r*")
plt.text(xi, yi, check_point_in_area(xi, yi), fontsize=10, bbox={'facecolor': 'yellow', 'alpha': 0.2})
lgnd = plt.legend([r'$y = x^2+2x-14$', r'$y = -x^2+2x+8$', r'$y = 2x+4$'], loc=2, shadow=True)
lgnd.get_frame().set_facecolor('#ffb19a')

plt.show()