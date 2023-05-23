import matplotlib.pyplot as plt


# Вводим функцию
def f(x):
    return x ** 2 + 2 * x + 1


# Вводим границы, а так же количество разбиений
a = int(input("Введите нижнюю границу: "))
b = int(input("Введите верхнюю границу: "))
n = int(input("Введите количество разбиений: "))


def simpsonmethod(f, a, b, n):
    x = 0
    dx = (b - a) / n  # ширина
    for i in range(n):
        x += dx / 6 * (f(a) + 4 * f((a + b) / 2) + f(b))  # Формула метода Симпсона
    return x


print(simpsonmethod(f, a, b, n))  # Вывод

print(simpsonmethod(f, a, b, 1))
print(simpsonmethod(f, a, b, 2))
print(simpsonmethod(f, a, b, 4))
print(simpsonmethod(f, a, b, 10))
print(simpsonmethod(f, a, b, 100))
print(simpsonmethod(f, a, b, 1000))

plt.axis([0, 1100, 60, 80])
plt.title('График точности метода Симпсона ', fontsize=20, fontname='Times New Roman')
plt.xlabel('Количество разбиений n', color='gray')
plt.ylabel('Значение функции', color='gray')
plt.text(1, simpsonmethod(f, a, b, 1), 'n = 1')
plt.text(2, simpsonmethod(f, a, b, 2), 'n = 2')
plt.text(4, simpsonmethod(f, a, b, 4), 'n = 4')
plt.text(10, simpsonmethod(f, a, b, 10), 'n = 10')
plt.text(100, simpsonmethod(f, a, b, 100), 'n = 100')
plt.text(1000, simpsonmethod(f, a, b, 1000), 'n = 1000')

plt.text(200, 65, r'$y = x^2+2x+1$', fontsize=20, bbox={'facecolor': 'yellow', 'alpha': 0.2})
plt.plot([1, 2, 4, 10, 100, 1000],
         [simpsonmethod(f, a, b, 1), simpsonmethod(f, a, b, 2), simpsonmethod(f, a, b, 4), simpsonmethod(f, a, b, 10),
          simpsonmethod(f, a, b, 100), simpsonmethod(f, a, b, 1000)], 'ro')
plt.show()
