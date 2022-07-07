from datetime import datetime
from termcolor import colored, cprint
# Пашка сын 01.12.2000
with open('Днюхи.txt') as f:
    lines=f.readlines()
for line in lines:
    line=line.strip()
    datte=line.split()[-1]
    datte2 = datetime.strptime(datte, "%d.%m.%Y")

    daays=(datetime.today() - datte2).days
    if daays%1000==0:
        color = 'green'
    elif 995<=daays%1000<1000:
        color = 'blue'
    elif 85<=daays%100<=100:
        color = 'yellow'
    elif 1<=daays%100<=3:
        color = 'red'
    else:
        color = 'white'
    cprint(f'{line}  прожил(а) уже {daays:,} дней ', color, end='')

    hourz = daays * 24
    strd=''
    if hourz%1000<=16 or 991<=hourz%1000:
        color = 'green'
    elif 930<=hourz%1000<=990:
        color = 'blue'
        strd= str(round((1000-hourz%1000)/24))
        strd=f'{strd} дней'
    elif 850<=hourz%1000<=929:
        color = 'yellow'
        strd= str(round((1000-hourz%1000)/24))
        strd = f'({strd} дней)'

    elif 1<=hourz%1000<=10:
        color = 'red'
    else:
        color = 'white'
    cprint(f'   или {hourz:,} часов {strd}  ', color,end='')

    strm=''
    minutes = hourz * 60
    if minutes%100000<=7000 or 99300<=minutes%100000:
        color = 'green'
    elif 97000<=minutes%100000<=99999:
        color = 'blue'
        strm = str(round((100000 - minutes%100000) / 24/60))
        strm = f'({strm} дней)'
    elif 93000<=minutes%100000<=97000:
        color = 'yellow'
        strm = str(round((100000 - minutes%100000) / 24/60))
        strm = f'({strm} дней)'
    elif 100<=minutes%100000<=1000:
        color = 'red'
    else:
        color = 'white'
    cprint(f' или {minutes:,} минут {strm}', color)

# def out_red(text):
#     print("\033[31m {}" .format(text))
# def out_yellow(text):
#     print("\033[33m {}" .format(text))
# def out_blue(text):
#     print("\033[34m {}" .format(text))
# out_red("Вывод красным цветом")
# out_yellow("Текст жёлтого цвета")
# out_blue("Синий текст")
#
#
# text = colored('Hello, Habr!', 'red', attrs=['blink'])
# print(text)
# cprint('Hello, Habr!', 'green')

# da='06.02.1979'
# da2="Настя Берега 18.04.1994"
# da25=da2.split()[-1]
# print(da25)

# day,month,year=da.split('.')
# print(day,month,year)
# dat=datetime.strptime(da,"%d.%m.%Y")
# dat25=datetime.strptime(da25,"%d.%m.%Y")
#
# print(dat.date())
# print(dat25.date())
#
# print(dat.strftime("%d %m %Y"))
# print(dat25.strftime("%d %m %Y"))
#
# tod=datetime.today()
#
# print(f'Сегодня {tod.strftime("%d %m %Y")}')
# a=tod-dat
# print(a.days)
# print(f'{da2}  прожила уже {(datetime.today()-dat25).days}')




