def fib_rec(N,f=[]):
    if N==1:
        return [1]
    elif N==2:
        return [1,1]
    k=fib_rec(N-1)
    d=fib_rec(N-2)

    return [*k,k[-1]+d[-1]]

N = int(input())
print(*fib_rec(N))