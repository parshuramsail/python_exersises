# Remove Matching element

# option->1
my_list = [2, 3, 4, 5, 3, 2]
element = 3
for i in my_list:
    if i == element:
        my_list.remove(i)
print(my_list)

# option->2
my_list = [2, 3, 4, 3, 3, 5, 3, 6]
remove_element = 3

if not my_list:
    print("Empty list")
elif my_list.count(remove_element) == 0:
    print("Not found")
else:
    for i in range(my_list.count(remove_element)):
        my_list.remove(remove_element)
print(my_list)
