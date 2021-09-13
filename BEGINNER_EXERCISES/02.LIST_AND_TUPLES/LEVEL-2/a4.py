# Second largest element in the list

my_list = [1, 3, 2, 3, 4, 5]

if my_list:
    remove_diplicates = list(set(my_list))
    remove_diplicates.remove(max(remove_diplicates))
    print(max(remove_diplicates))
else:
    print("list is empty")
