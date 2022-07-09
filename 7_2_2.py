def is_triangle(a,b,c):
    print('1: ', ( a + b + c - max(a, b, c) ) > max(a, b, c)  )
    print('2: ', max(a, b, c) )
    print('3: ',a + b + c - max(a, b, c))
    return  a + b + c - max(a, b, c)  > max(a, b, c)

def le(s):
    return s,len(s)

x=input().split()
print(x)
d={le(i)[0]:le(i)[1] for i in x}
print(d)
a = sorted(d, key=lambda x: d[x])
print(*a)

