def layer_kol(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 4
    if n==3:
        return 9
    return n**2

def pyramid_height(n):
    x=0
    kol=0
    while n>x+layer_kol(kol):
        x+=layer_kol(kol)
        kol+=1
    return kol

for n in range(1, 50, 3):
    print (pyramid_height(n))