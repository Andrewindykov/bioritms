def f(x):
    return 0.5 * pow(x, 2) - 2.0

a,b=map(int,input().split())

gen = ( f(i/100) for i in range(a*100,b*100+1) )

for _ in range(20):
    print(round(next(gen),2), end=" ")


