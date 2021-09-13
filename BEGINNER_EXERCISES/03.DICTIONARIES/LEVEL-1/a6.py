# MIN value in the dictionary

my_dict = {'a': 4, 'b': 3, 'c': 7}
if my_dict:
    max_value = min(set(my_dict.values()))
    print(max_value)
else:
    print(None)
