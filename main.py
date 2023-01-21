import random
import time
from datetime import datetime

grey = 'grey'
white = 'white'
magenta = 'magenta'
yellow = 'yellow'
blue = 'blue'
green = 'green'
red = 'red'

rred = '\u001b[31m'
nocolor = '\u001b[0m'


def c(colo: str):
    def c_deco(func):
        def co(*args, **kwargs):
            if colo == 'grey':
                colors = '\u001b[30;1m'  # grey'
            elif colo == 'white':
                colors = '\u001b[37m'  # white'
            elif colo == 'magenta':
                colors = '\u001b[35m'  # 'magenta'
            elif colo == 'yellow':
                colors = '\u001b[33m'  # 'yellow'
            elif colo == 'blue':
                colors = '\u001b[34m'  # 'blue'
            elif colo == 'green':
                colors = '\u001b[34m'  # 'green'
            elif colo == 'red':
                colors = '\u001b[31m'  # 'red'
            else:
                colors = '\u001b[37m'  # white'

            print(colors, end='')
            result = func(*args, **kwargs)
            print('\u001b[0m', end='')
            return result

        return co

    return c_deco


def gisto(n):
    ymax = max(n)

    for y in range(1, ymax + 1):
        print('                   ', end='')
        for nk in n:

            if nk < 4:
                color = '\u001b[30;1m'  # grey'
            elif nk < 5:
                color = '\u001b[37m'  # white'
            elif nk < 6:
                color = '\u001b[35m'  # 'magenta'
            elif nk < 7:
                color = '\u001b[33m'  # 'yellow'
            elif nk < 8:
                color = '\u001b[34m'  # 'blue'
            else:
                color = '\u001b[32m'  # green

            if nk >= ymax - y + 1:
                print(color, end='*       ')
                print(nocolor, end='')
            else:
                print(end='        ')
        print(' ')


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
        col = '\u001b[32m'
        ou = f'{i:,}{s}'

    elif int(nice * 0.99) <= i % nice < nice:
        col = '\u001b[34m'
        ddd = round((nice - i % nice) / ind, 2)

        ou = f'{i:,}{s} (after {ddd:} d)'
    elif int(nice * 0.9) <= i % nice <= int(nice * 0.99):
        col = '\u001b[33m'
        ddd = round((nice - i % nice) / ind, 2)
        ou = f'{i:,}{s} (in {ddd:} d)'

    elif 0 < i % nice <= nice // 100:
        col = '\u001b[31m'
        ddd = round((i % nice) / ind, 1)
        ou = f'{i:,}{s} ({ddd:} d ago)'

    else:
        col = random.choice(['\u001b[37m', '\u001b[37m', '\u001b[37m', '\u001b[37m'])
        ou = f'{i:,}{s}'

    return ou, col


t = False

with open('Днюхи.txt') as f:
    lines = f.readlines()
# print('\u001b[31m')  # 'red'
# print('red rat')
# print('\u001b[0m')
k = True
for line in lines:
    # print(line)
    line = line.strip()
    datte = line.split(' ')[-1]
    # print(datte,type(datte))
    datte2 = datetime.strptime(datte, "%d.%m.%Y")

    # print(datte2, type(datte2), datetime.today())

    daays = (datetime.today() - datte2).days
    #  print((' 1:', daays, daays % 1000) if t else '', end='')

    if k:
        k = False
        masterdatte = datte2
        masterdaays = daays

    out, color = colored(daays, 'd')
    # print(f"--------------------{color}")
    print(f'{line}  {color}{out}{nocolor} ', end='')

    out, color = colored(daays, 'h', h=5)
    print(f' {color} ={out}{nocolor}', end='')

    out, color = colored(daays, 'm', h=2, m=4)
    print(f' {color} ={out}{nocolor}', end='')

    out, color = colored(daays, 's', h=2, m=4, sec=25)
    print(f' {color} ={out}{nocolor}', end='')

    ye = int(daays) / 365
    ye7 = ye / 7
    print(f' {ye:.3} y  {ye7:.3} coils', end=' ')

    if ye7 - int(ye7) < 0.05:
        print(f' {rred}gals{nocolor}', end=' ')
    print()
    sov_list = (23.6884, 28.426125, 33.163812, 37.901499, 42.6392, 47.3769, 52.1146)
    xx = abs(daays - masterdaays)
    a = [xx % i for i in sov_list]
    b = [abs(round(100 - (xx % i) / i * 200)) for i in sov_list]
    #print(a, b, sep="\n")
    # a1 = xx % sov1
    # b1 = abs(round(100 - a1 / sov1 * 200))
    # a2 = xx % sov2
    # b2 = abs(round(100 - a2 / sov2 * 200))
    # a3 = xx % sov3
    # b3 = abs(round(100 - a3 / sov3 * 200))
    # a4 = xx % sov4
    # b4 = abs(round(100 - a4 / sov4 * 200))
    #
    # a5 = xx % sov5
    # b5 = abs(round(100 - a5 / sov5 * 200))
    # a6 = xx % sov6
    # b6 = abs(round(100 - a6 / sov6 * 200))
    # a7 = xx % sov7
    # b7 = abs(round(100 - a7 / sov7 * 200))
    # overall = round((b1 + b2 + b3 + b4 + b5 + b6 + b7) / 7)
    overall = round(sum(b) / 7)
    # print(f'{xx} muladh={b1} emo={b2} intell={b3} heart={b4} creat={b5} intuit={b6} sahasrar={b7} ', end=' ')  # совместимость


    if overall < 40:
        color = '\u001b[30;1m'  # grey'
    elif overall < 50:
        color = '\u001b[37m'  # white'
    elif overall < 60:
        color = '\u001b[35m'  # 'magenta'
    elif overall < 70:
        color = '\u001b[33m'  # 'yellow'
    elif overall < 80:
        color = '\u001b[34m'  # 'blue'
    else:
        color = '\u001b[32m'  # green

    print(f'{color}overall:{overall}{nocolor}', end='   ')

    print(f'  telo={b[0]} emo={b[1]} intell={b[2]} heart={b[3]} creat={b[4]} intuit={b[5]} sahasrar={b[6]} ',
          end='  \n')  # совместимость
    # print(f'\u001b[32moverall:{overall} {nocolor}')
    print()
    if line[0] == '+' or (overall > 70 and overall < 100) or 220 < b[0] + b[1] + b[2] < 300:
        # gisto([b1 // 10, b2 // 10, b3 // 10, b4 // 10, b5 // 10, b6 // 10, b7 // 10])
        gisto(list(map(lambda  x: x//10, b)))

    # print()
    # print(pifprint(pif(datte)), )
    # time.sleep(7)

    # https://goroskop365.ru/data-rozhdeniya/21-fevralya-1994-god/
    # https://in-contri.ru/
