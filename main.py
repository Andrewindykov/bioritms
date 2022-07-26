from datetime import datetime
from termcolor import cprint
import time
def colored(d, s, h=0, m=0, sec=0):
    ''' раскрашиваем вывод за 10%, 1% до и 1% после события и считаем это в днях на входе возраст'''

    if s == 'd':
        nice = 1000
        i = d
        ind = 1

    elif s == 'h':
        nice = 10_000
        i = d * 24 + h
        ind = 24

    elif s == 'm':
        nice = 1_000_000
        i = (d * 24 + h) * 60 + m
        ind = 24 * 60

    elif s == 's':
        nice = 100_000_000
        i = ((d * 24 + h) * 60 + m) * 60 + sec
        ind = 24 * 60 * 60

    else:
        i = 0
        nice = 1

    if i % nice <= nice // 1000:
        col = 'green'
        ou = f'{i:,}{s}'

    elif int(nice * 0.99) <= i % nice < nice:
        col = 'blue'
        ddd = round((nice - i % nice) / ind, 2)

        ou = f'{i:,}{s} (через {ddd:} д)'
    elif int(nice * 0.9) <= i % nice <= int(nice * 0.99):
        col = 'yellow'
        ddd = round((nice - i % nice) / ind, 2)
        ou = f'{i:,}{s} (через {ddd:} д)'

    elif 0 < i % nice <= nice // 100:
        col = 'red'
        ddd = round((i % nice) / ind, 1)
        ou = f'{i:,}{s} (прошло {ddd:} д)'

    else:
        col = 'white'
        ou = f'{i:,}{s}'

    return ou, col


def pif(date):
    ''' вычисляет числа пифагора по строке рождения'''
    sl = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    a = 0
    for i in date:
        if i in '123456789':
            a += int(i)
            sl[i] += 1
    if a in (11, 22, 33):
        cprint(f' сумма={a}', 'yellow')
    else:
        print()
    x = a % 10
    if x != 0:
        sl[str(x)] += 1
    if a >= 10:
        x = a // 10
        if x != 0:
            sl[str(x)] += 1
    # print(sl)
    return sl


def pifprint(sl):
    digits = ''
    #   print(sl)
    k = 0
    for i in '147258369':
        # print(item, end='+')
        digits += f'{i * sl[i]:4} '
        k += 1
        if str(k) in '36':
            digits += '\n'
    #      res
    return digits


t = False
# Пашка сын 01.12.2000
with open('Днюхи.txt') as f:
    lines = f.readlines()
for line in lines:
    #print(line)
    line = line.strip()
    datte = line.split(' ')[-1]
    # print(datte,type(datte))
    datte2 = datetime.strptime(datte, "%d.%m.%Y")
    # print(datte2, type(datte2), datetime.today())

    daays = (datetime.today() - datte2).days
    #  print((' 1:', daays, daays % 1000) if t else '', end='')

    out, color = colored(daays, 'd')
    cprint(f'{line}  {out}', color, end='')

    out, color = colored(daays, 'h', h=5)
    cprint(f'  ={out}', color, end='')

    out, color = colored(daays, 'm', h=2, m=4)
    cprint(f'  ={out}', color, end='')

    out, color = colored(daays, 's', h=2, m=4, sec=25)
    cprint(f'  ={out}', color, end='')

    ye=int(daays)/365
    ye7=ye/7
    print(f' {ye:.3} лет  {ye7:.3} семилетних циклов', end='')
    if ye7 - int(ye7) < 0.05:
        cprint(f' галс', 'red', end='')

    print(pifprint(pif(datte)))
time.sleep(5)

# https://goroskop365.ru/data-rozhdeniya/21-fevralya-1994-god/