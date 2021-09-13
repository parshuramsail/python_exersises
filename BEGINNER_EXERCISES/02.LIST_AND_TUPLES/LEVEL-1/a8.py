# Count the elements grater than 3

# option->1
my_list = [1, 4, 3, 2, 7, -2]
count = 0
for i in my_list:
    if i > 3:
        count += 1
print(count)

# option->2
my_list = [10, 11, 2, 0, 12, 13]
count = sum(1 for i in my_list if i > 3)
print(count)
