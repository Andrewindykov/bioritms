names = list(input().lower().split())
print(names)
i, k = 0, 0
while i < len(names):
    if names[i][0] == names[i][-1]:
        k = i + 1
        break
    i+=1
if k != 0:
    print("ДА")
else:
    print("НЕТ")
