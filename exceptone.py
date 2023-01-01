arr = [ 0, 0, 0.55, 0, 0 ]
a=arr[0]
b=arr[1]
c=arr[2]
n=a
if not(a==b==c):
    print(666)
    if a==b:
        n=c
    #    print(777)
    elif a==c:
        n=b
      #  print(8888)
    elif b==c:
        n=a
        print(999)
else:
    for i in range(len(arr)):
        # print(arr[i])
        if arr[i] !=n:
            a=arr[i]
            break
a=n
print(a)

