# Flatten a list that contains list

my_list = [[1, 2, 3], 11, [4, 5, 6], [7, 8, 9]]
flatten_list = []

for i in my_list:
    if isinstance(i, list):
        for j in i:
            flatten_list.append(j)
    else:
        flatten_list.append(i)
print(flatten_list)
