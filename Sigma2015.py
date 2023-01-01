A = [12, 45,  5, 3, 17, 23, 21, 20, 19, 18, 17]

A = [45,  5, 3, 17, 23, 21, 20, 19, 18 ]

proiz=1000001
for i,x in enumerate(A):
    print(f"{i=} {x=}  ")
    for j, x2 in enumerate(A):
        j2=j
        print(f" {j2=} {x2=}", end=' ')
        if abs(j2-i) >= 6:
            print('Произведение = ', x*x2)
            if (x*x2<proiz) and ((x*x2)%2==0):
                proiz=x*x2
                print('присвоили', proiz)
        else:
            print(f"no", end=' ')
    print()

print('ответ', proiz)

