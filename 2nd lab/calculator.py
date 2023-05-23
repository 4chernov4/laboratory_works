a = float(input('Введите 1 число: '))
c = input('Введите знак: ')
b = float(input('Введите 2 число: '))

if c == '+':
    l = a + b
    print(l)
elif c == '-':
    l = a - b
    print(l)
elif c == '*':
    l = a * b
    print(l)
elif c == '/':
    if b == 0:
        print('На ноль делить нельзя')
    else:
        l = a / b
        print(l)
else:
    print('Введите знак!')
