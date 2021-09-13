# Check all values are equal

my_dict = {'a': 4, 'b': 4, 'c': 4, 'd': 4}

unique_values = set(my_dict.values())

if len(unique_values) == 0:
    print("empty")
elif len(unique_values) == 1:
    print(True)
else:
    print(False)
