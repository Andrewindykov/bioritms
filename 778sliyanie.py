def sli(k):
    sor = []
    if len(k) <= 1:
        sor = k
    else:
        i = len(k) // 2

        a = sli(k[:i])
        b = sli(k[i:])

        i = j = 0
        while i <= len(a) and j <= len(b):
            if a[i] < b[j]:
                sor.append(a[i])
                i += 1
                if i == len(a):
                    sor.extend(b[j:])
                    break
            else:
                sor.append(b[j])
                j += 1
                if j == len(b):
                    sor.extend(a[i:])
                    break
    return sor


s = list(map(int, input().split()))
print(*sli(s))
