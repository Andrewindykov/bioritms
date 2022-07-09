from datetime import datetime
from termcolor import cprint

# Пашка сын 01.12.2000
with open('Днюхи.txt') as f:
    lines = f.readlines()
for line in lines:
    line = line.strip()
    datte = line.split()[-1]
    datte2 = datetime.strptime(datte, "%d.%m.%Y")

    daays = (datetime.today() - datte2).days
    if daays % 1000 == 0:
        color = 'green'
    elif 995 <= daays % 1000 < 1000:
        color = 'blue'
    elif 85 <= daays % 100 <= 100:
        color = 'yellow'
    elif 1 <= daays % 100 <= 3:
        color = 'red'
    else:
        color = 'white'
    cprint(f'{line}  прожил(а) уже {daays:,} дней ', color, end='')

    hourz = daays * 24
    strd = ''
    if hourz % 1000 <= 16 or 991 <= hourz % 1000:
        color = 'green'
    elif 930 <= hourz % 1000 <= 990:
        color = 'blue'
        strd = str(round((1000 - hourz % 1000) / 24))
        strd = f'{strd} дней'
    elif 850 <= hourz % 1000 <= 929:
        color = 'yellow'
        strd = str(round((1000 - hourz % 1000) / 24))
        strd = f'({strd} дней)'

    elif 1 <= hourz % 1000 <= 10:
        color = 'red'
    else:
        color = 'white'
    cprint(f'   или {hourz:,} часов {strd}  ', color, end='')

    strm = ''
    minutes = hourz * 60
    if minutes % 100000 <= 7000 or 99300 <= minutes % 100000:
        color = 'green'
    elif 97000 <= minutes % 100000 <= 99999:
        color = 'blue'
        strm = str(round((100000 - minutes % 100000) / 24 / 60))
        strm = f'({strm} дней)'
    elif 93000 <= minutes % 100000 <= 97000:
        color = 'yellow'
        strm = str(round((100000 - minutes % 100000) / 24 / 60))
        strm = f'({strm} дней)'
    elif 100 <= minutes % 100000 <= 1000:
        color = 'red'
    else:
        color = 'white'
    cprint(f' или {minutes:,} минут {strm}', color)

