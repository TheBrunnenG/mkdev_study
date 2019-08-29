import random

lastID = 10  # тут последний ID новости упорядоченного списка
new_list = []
for i in range(3):
    a = random.randint(0, lastID)
    new_list.append(a)
print(new_list)
