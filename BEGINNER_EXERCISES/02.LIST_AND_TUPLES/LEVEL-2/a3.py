# Print common Elements in two list

list_A = [1, 2, 3, 4]
list_B = [3, 4]
common = []

for i in list_A:
    if i in list_B:
        common.append(i)
print(common)
