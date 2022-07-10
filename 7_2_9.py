def proizv(a,b):
    return a*b
x=list( map( int, input().split() ) )
print(proizv(max(x), min(x)))