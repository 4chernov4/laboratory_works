import matplotlib.pyplot as plt


# Вводим функцию
def f(x):
    return x ** 2 + 2 * x + 1


# Вводим границы, а так же количество разбиений
divn = int(input('Введите n: '))
ainput = int(input('Введите нижнюю границу:'))
binput = int(input('Введите верхнюю границу:'))


def rectangle(f, a, b, n):
    x = 0
    dx = (b - a) / n  # ширина
    for i in range(n):
        x += dx * f(a + dx / 2 + i * dx)  # Формула метода прямоугольников
    return x


print(rectangle(f, ainput, binput, divn))  # Вывод

print(rectangle(f, ainput, binput, 1))
print(rectangle(f, ainput, binput, 2))
print(rectangle(f, ainput, binput, 4))
print(rectangle(f, ainput, binput, 10))
print(rectangle(f, ainput, binput, 100))
print(rectangle(f, ainput, binput, 1000))

plt.axis([0, 1100, 60, 80])
plt.title('График точности метода Прямоугольников', fontsize=20, fontname='Times New Roman')
plt.xlabel('Количество разбиений n', color='gray')
plt.ylabel('Значение функции', color='gray')
plt.text(1, rectangle(f, ainput, binput, 1), 'n = 1')
plt.text(2, rectangle(f, ainput, binput, 2), 'n = 2')
plt.text(4, rectangle(f, ainput, binput, 3), 'n = 4')
plt.text(10, rectangle(f, ainput, binput, 10), 'n = 10')
plt.text(100, rectangle(f, ainput, binput, 100), 'n = 100')
plt.text(1000, rectangle(f, ainput, binput, 1000), 'n = 1000')

plt.text(200, 65, r'$y = x^2+2x+1$', fontsize=20, bbox={'facecolor': 'yellow', 'alpha': 0.2})
plt.plot([1, 2, 4, 10, 100, 1000],
         [rectangle(f, ainput, binput, 1), rectangle(f, ainput, binput, 2), rectangle(f, ainput, binput, 4),
          rectangle(f, ainput, binput, 10), rectangle(f, ainput, binput, 100), rectangle(f, ainput, binput, 1000)],
         'ro')
plt.show()
