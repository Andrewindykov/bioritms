a=int(input())
b=[abs(i) for i in range(-a,a+1)]
c=[val**3 for i,val in enumerate(b) if i<4]
print(*c)
