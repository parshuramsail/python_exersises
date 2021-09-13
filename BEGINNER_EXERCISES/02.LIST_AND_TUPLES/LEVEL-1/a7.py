# Remove duplicates from a list

# option->1  this method changes the order of list elements
my_list = ['a', 'b', 'c', 'a']
print(list(set(my_list)))

# option->2 this method does not changes the order of the list elements
my_list = [1, 1, 2, 3, 4, 4]
no_duplicates = list(dict.fromkeys(my_list))
print(no_duplicates)
