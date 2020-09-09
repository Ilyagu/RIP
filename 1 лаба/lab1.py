from math import sqrt

while (True):
    try:
        a = int(input('Введите коэфициент a: '))
        b = int(input('Введите коэфициент b: '))
        c = int(input('Введите коэфициент c: '))
        p=5/a+5/b+5/c
    except ValueError:
        print('Это не число, введите повторно.\n')
    except ZeroDivisionError:
        print('Нули не могут быть коэфициентами, введите повторно.\n')
    else:
        break
bs = ""
if b > 0:
    bs = '+'
cs = ''
if c > 0:
    cs = '+'
print(f'Ваше уравнение {a}x^4{bs}{b}x^2{cs}{c}=0\n')
d = b ** 2 - 4 * a * c
if d < 0:
    print('Нет действительныйх корней')
elif d == 0:
    x1 = -b / (2 * a)
    if x1 < 0:
        print('Нет действительныйх корней')
    else:
        x1 = sqrt(x1)
        print(f'Корни уравнения:\n{x1}\n-{x1}')
else:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    if x1 < 0 and x2 < 0:
        print('Нет действительныйх корней')
    elif x1 < 0:
        x2 = sqrt(x2)
        print(f'Корни уравнения:\n{x2}\n-{x2}')
    else:
        x1 = sqrt(x1)
        print(f'Корни уравнения:\n{x1}\n-{x1}')
        if x2 >= 0:
            x2 = sqrt(x2)
            print(f'\n{x2}\n-{x2}')
