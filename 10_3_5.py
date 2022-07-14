import sys
import random

# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
print('lst_in=', lst_in)

lst2 = []
for row in lst_in:
    row_int = list(map(int, row.split()))
    lst2 += [row_int]
print('lst2=', lst2)

lst = list(zip(*map(str.split, lst_in)))
print('lst=', lst)
lst33 = list(map(str.split, lst_in))
print('lst33=', lst33)
random.shuffle(lst)
[print(*i) for i in zip(*lst)]

lst3 = []
for i in zip(*lst2):
    k = list(i)
    lst3.append(k)

print('lst3=', lst3)

random.shuffle(lst3)

print('lst3= после', lst3)

for i in zip(*lst3):
    print(*i)
