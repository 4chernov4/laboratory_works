# Вызываем библиотеку
import numpy as np
import matplotlib.pyplot as plt

# Вводим значение начального приближения
x0 = float(input('Введите начальное приближение х0: '))


# Вводим функцию
def f(x):
    return np.cos(x) - x ** 3


# Вводим производную функции
def df(x):
    return -np.sin(x) - 3 * (x ** 2)


abc = []    #инициализация массива


# Метод Ньютона
def newtonmethod(func, dfunc, xmain, limitation=1e-9):  # Limitation=1e-9 Погрешность в экспотенциальной форме
    x = xmain
    while abs(func(x)) >= limitation:  # Условие остановки
        if dfunc(x) == 0:  # Условие деления на 0
            break
        x = x - func(x) / dfunc(x)
        abc.append(x)   #добавить значения х в массив
    return x


# Вывод
print(newtonmethod(f, df, x0))
for i in range(len(abc)):   #итерация по массиву
    print('x= ', abc[i], ' y= ', f(abc[i]))

plt.axis([-20, 20, -20, 20])
plt.title('Метод Ньютона ', fontsize=20, fontname='Times New Roman')
plt.xlabel('Ось х ', color='gray')
plt.ylabel('Ось у ', color='gray')
plt.grid(True)
xvalue = np.linspace(-3, 3, 100)
plt.plot(xvalue, f(xvalue))
plt.plot(xvalue, df(xvalue))
plt.plot(newtonmethod(f, df, x0))
for i in range(len(abc)):
    plt.plot(abc[i], f(abc[i]), 'ro')
    plt.plot(f(abc[i]), abc[i], 'b*')
plt.show()
