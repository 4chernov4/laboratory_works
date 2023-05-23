#Вызываем библиотеку
import math

#Вводим значение начального приближения
x0 = float(input('Введите начальное приближение х0: '))


#Вводим функцию
def f(x):
    return math.cos(x) - x ** 3


#Вводим производную функции
def df(x):
    return -math.sin(x) - 3 * (x ** 2)

#Метод Ньютона
def newtonmethod(func, dfunc, xmain, limitation=1e-9):  #Limitation=1e-9 Погрешность в экспотенциальной форме
    x = xmain
    while abs(func(x)) >= limitation:   #Условие остановки
        if dfunc(x) == 0:   #Условие деления на 0
            break
        x = x - func(x) / dfunc(x)
    return x

#Вывод
print(newtonmethod(f, df, x0))