#    Москва Уфа Тула Самара Омск Воронеж Владивосток Лондон Калининград Севастополь
# их в 3 столбца N строк

lst=input().split()

z = zip(lst[::3], lst[1::3], lst[2::3])
[print(*i) for i in z]



