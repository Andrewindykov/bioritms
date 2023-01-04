n = list(map(int, input().split()))

xmax = len(n)
ymax = max(n)

for y in range(1, ymax + 1):
    #print(end='*')
    for nk in n:
        if nk >= ymax - y + 1:
            print(end='* ')
        else:
            print(end='  ')
    print(' ')