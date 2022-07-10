import sys
# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
for i in lst_in:
    key,val=i.split('=')
    menu={**menu, key:val}
print(menu)
