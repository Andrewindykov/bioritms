from string import ascii_lowercase

x = (i + j
     for i in ascii_lowercase
     for j in ascii_lowercase)
print(*(next(x) for _ in range(50)))