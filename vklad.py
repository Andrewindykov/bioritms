import random
A = [3, 5,  6, 5, 2, 2]
B = [3, 12, 9, 3, 2, 0]
A=[3,3,3,3,3,3]
B=[3,3,3,3,3,3]
D = []
s=0
D_min=50000
for i in range(6):
    print(A[i], B[i], end='  ')
    x=random.choice([A[i], B[i]])
    x=max(A[i], B[i])
    delta=abs(A[i]-B[i])
    if delta>0 and delta % 3 != 0:
        D.append(delta)
        if delta<D_min:
            D_min=delta
    print(f"{x=}, {delta=} {D_min=}")
    s+=x
print(s, "делится на 3" if s%3==0 else "не делится на 3. Подходит")
print("массив D = ", D)

d2=0
if s%3!=0:
    print('Ответ: ', s)
else:
    if D_min<50000:
        print('Ответ: ', s - D_min)
    else:
        print("Ответ", 0)
    print()
    print()

    if len(D)>0:
        d2=min(D)
    print(f"{d2=}")
    if d2>0:
        print( 'Ответ: ', s-d2)
    else:
        print(0)