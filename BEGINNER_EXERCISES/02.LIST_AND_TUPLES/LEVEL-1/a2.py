# Print elements on the same line without commas

# option->1
my_list = [1, 2, 3, 4, 5]
for i in my_list:
    print(i, end=" ")

# option->2
my_list = [1, 2, 3, 4, 5]
print(*my_list, sep=" ")
