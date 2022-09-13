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

        ou = f'{i:,}{s} (after {ddd:} d)'
    elif int(nice * 0.9) <= i % nice <= int(nice * 0.99):
        col = 'yellow'
        ddd = round((nice - i % nice) / ind, 2)
        ou = f'{i:,}{s} (in {ddd:} d)'

    elif 0 < i % nice <= nice // 100:
        col = 'red'
        ddd = round((i % nice) / ind, 1)
        ou = f'{i:,}{s} ({ddd:} d ago)'

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
        cprint(f' sum={a}', 'yellow')
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
k = True
for line in lines:
    #print(line)
    line = line.strip()
    datte = line.split(' ')[-1]
    #print(datte,type(datte))
    datte2 = datetime.strptime(datte, "%d.%m.%Y")

    #print(datte2, type(datte2), datetime.today())

    daays = (datetime.today() - datte2).days
    print((' 1:', daays, daays % 1000) if t else '', end='')

    if k:
        k = False
        masterdatte = datte2
        masterdaays = daays

    out, color = colored(daays, 'd')
    cprint(f'{line}  {out} ', color, end='')

    out, color = colored(daays, 'h', h=5)
    cprint(f'  ={out}', color, end='')

    out, color = colored(daays, 'm', h=2, m=4)
    cprint(f'  ={out}', color, end='')

    out, color = colored(daays, 's', h=2, m=4, sec=25)
    cprint(f'  ={out}', color, end='')

    ye = int(daays) / 365
    ye7 = ye / 7
    print(f' {ye:.3} y  {ye7:.3} coils')
    if ye7 - int(ye7) < 0.05:
        cprint(f' gals', 'red', end=' ')
    sov1=23.6884
    sov2=28.426125
    sov3=33.163812
    sov4=37.901499
    sov5=42.6392
    sov6=47.3769
    sov7=52.1146
    xx=abs(daays - masterdaays)
    a1 = xx%sov1
    b1=abs(round(100-a1/sov1*200))
    a2 = xx%sov2
    b2=abs(round(100-a2/sov2*200))
    a3 = xx%sov3
    b3=abs(round(100-a3/sov3*200))
    a4 = xx%sov4
    b4=abs(round(100-a4/sov4*200))

    a5 = xx % sov5
    b5 = abs(round(100 - a5 / sov5 * 200))
    a6 = xx % sov6
    b6 = abs(round(100 - a6 / sov6 * 200))
    a7 = xx % sov7
    b7 = abs(round(100 - a7 / sov7 * 200))
    overall=round((b1+b2+b3+b4+b5+b6+b7)/7)
    print(f'{xx} muladh={b1} emo={b2} intell={b3} heart={b4} creat={b5} intuit={b6} sahasrar={b7} ', end=' ')  # совместимость

    #print(f'  muladh={b1} emo={b2} intell={b3} heart={b4} creat={b5} intuit={b6} sahasrar={b7} ', end=' ')  # совместимость

    if overall<40:
        color='grey'
    elif overall<50:
        color = 'white'
    elif overall<60:
        color = 'magenta'
    elif overall < 70:
        color = 'yellow'
    elif overall < 80:
        color = 'blue'
    else:
        color = 'green'


    cprint(f'overall:{overall}', color, end='     ')
    #cprint(f'overall:{overall}', color)
    #print()

    print(pifprint(pif(datte)), )
    print()

time.sleep(7)

# https://goroskop365.ru/data-rozhdeniya/21-fevralya-1994-god/
# https://in-contri.ru/