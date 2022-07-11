from datetime import datetime
from termcolor import cprint


def colored(d, s, h=0, m=0, sec=0):
    ''' раскрашиваем вывод за 3%, 1% до и 1% после события и считаем это в днях на входе возраст'''

    if s == 'd':
        nice = 1000
        i = d
        ind = 1
    elif s == 'h':
        nice = 50000
        i = d * 24 + h
        ind = 24
    elif s == 'm':
        nice = 500000
        i = (d * 24 + h) * 60 + m
        ind = 24 * 60
    elif s == 's':
        nice = 100000000
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
        ddd = round((nice - i % nice)/ind, 1)

        ou = f'{i:,} (через {ddd:,} д)'
    elif int(nice * 0.97) <= i % nice <= int(nice * 0.99):
        col = 'yellow'
        ddd = round((nice - i % nice)/ind, 1)
        ou = f'{i:,} (через {ddd:,} д)'
    elif 0 < i % nice <= nice // 100:
        col = 'red'
        ddd = round((i % nice)/ind, 1)
        ou = f'{i:,} (прошло {ddd:,} д)'
    else:
        col = 'white'
        ou = f'{i:,}{s}'

    return ou, col


t = False
# Пашка сын 01.12.2000
with open('Днюхи.txt') as f:
    lines = f.readlines()
for line in lines:
    line = line.strip()
    datte = line.split()[-1]
    datte2 = datetime.strptime(datte, "%d.%m.%Y")

    daays = (datetime.today() - datte2).days
    print((' 1:', daays, daays % 1000) if t else '', end='')

    out, color = colored(daays, 'd')
    cprint(f'{line}  {out}', color, end='')

    out, color = colored(daays, 'h', h=5)
    cprint(f'  ={out}', color, end='')

    out, color = colored(daays, 'm', h=2, m=4)
    cprint(f'  ={out}', color, end='')

    out, color = colored(daays, 's', h=2, m=4, sec=25)
    cprint(f'  ={out}', color, end='\n')

    # hourz = daays * 24
    # strd = ''
    # ddd = round((1000 - hourz % 1000) / 24, 1)
    # strd = str(ddd)
    # print((' 2:', hourz, hourz % 1000, ' d ', ddd) if t else '', end='')
    # if hourz % 1000 <= 16 or 991 <= hourz % 1000:
    #     color = 'green'
    # elif 930 <= hourz % 1000 <= 990:
    #     color = 'blue'
    #     strd = str(round((1000 - hourz % 1000) / 24))
    #     strd = f'{strd} д'
    # elif 850 <= hourz % 1000 <= 929:
    #     color = 'yellow'
    #     strd = str(round((1000 - hourz % 1000) / 24))
    #     strd = f'({strd} д)'
    #
    # elif 1 <= hourz % 1000 <= 10:
    #     color = 'red'
    # else:
    #     color = 'white'
    # cprint(f'= {hourz:,} ч ({strd} д до {int(hourz//1000)+1} тыс)  ', color, end='')
    #
    # strm = ''
    # minutes = hourz * 60
    # print((' 3m', minutes, minutes % 100000, ' ') if t else '', end='')
    #
    # print((hourz, hourz % 1000) if t else '', end='')
    # ddd = (1000000 - (minutes % 1000000)) / 24
    # strm = str(round(ddd / 60 , 1))
    # print(('  ' + strm) if t else '', end='')
    #
    # if minutes % 100000 <= 7000 or 99300 <= minutes % 100000:
    #     color = 'green'
    # elif 97000 <= minutes % 100000 <= 99999:
    #     color = 'blue'
    #     strm = f'({strm} дней)'
    # elif 73000 <= minutes % 100000 <= 97000:
    #     color = 'yellow'
    #     ddd = (1000000 - (sec % 1000000)) / 24
    #     strm = str(round(ddd / 60, 1))
    #     strm = f'({strm} дней)'
    # elif 100 <= minutes % 100000 <= 1000:
    #     color = 'red'
    # else:
    #     color = 'white'
    # cprint(f' = {minutes:,} м ({strm} д до) ', color, end='')
    #
    # strm = ''
    # sec = minutes * 60
    # if sec % 1000000 <= 70000 or 993000 <= sec % 1000000:
    #     color = 'green'
    # elif 970000 <= sec % 1000000 <= 999999:
    #     color = 'blue'
    #     strm = str(round((1000000 - sec % 1000000) / 24 / 60 / 60,2))
    #     strm = f'({strm} д)'
    # elif 730000 <= sec % 1000000 <= 970000:
    #     color = 'yellow'
    #     ddd = (1000000 - (sec % 1000000)) / 24
    #     strm = str(round(ddd / 60 / 60, 1))
    #     strm = f'({strm} д)'
    # elif 1000 <= sec % 1000000 <= 10000:
    #     color = 'red'
    # else:
    #     color = 'white'
    # cprint(f' = {sec:,} с {strm}', color)
