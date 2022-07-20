import numpy as np
import sys
# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

row,col=(int(x) for x in lst_in[0].split())
a1 = ([int(x) for x in lst_in[1+i].split()] for i in range(row) )
mat1=np.array(list(a1))
print(mat1)

a2=([int(x) for x in lst_in[2+row+i].split()] for i in range(row) )
mat2=np.array(list(a2))
print(mat2)

mat3 = mat1 + mat2

for i in mat3:
    print(*i)
