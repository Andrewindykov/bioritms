list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
for i in enumerate(list1):
    print(i)


cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]


gen = (cities[j%len(cities)] for j in range(1000000))

for _ in range(20):
    print(next(gen), end=" ")