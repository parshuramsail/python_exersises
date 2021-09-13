# Check if list is empty or not

# option->1
my_list = []
if my_list:
    print("not empty")
else:
    print("empty")

# option->2
my_list = [1, 2, 3, 4]
if len(my_list) == 0:
    print("empty")
else:
    print("not empty")
