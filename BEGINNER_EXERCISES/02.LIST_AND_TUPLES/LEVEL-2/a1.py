# Diffrence between two lists

list_a = [1, 3, 4, 5]
list_b = [1, 3]
diffrence = []

for i in list_a:
    if i not in list_b:
        diffrence.append(i)
print(diffrence)
