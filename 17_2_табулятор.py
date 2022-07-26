f = open('prices.txt', 'r')
strs=f.readlines()
s=0
for i in strs:
    a,b,c=list(i.split("\t"))
  #  print(a,b,c)
    s+=int(b)*int(c)
print("s=",s)
with open('input.txt', encoding='utf-8') as file:
    print('Repeat after me:', file.readline().strip())
    for line in file:
        print(line.strip() + '!')