# Frequency of the values in the list

my_dict = {
    'a': 4,
    'b': 4,
    'c': 2,
    'd': 7,
    'e': 4,
    'f': 2,
    'g': 7,
    'h': 7,
}

frquency_dict = {}

for value in my_dict.values():
    if value in frquency_dict:
        frquency_dict[value] += 1
    else:
        frquency_dict[value] = 1
print(frquency_dict)
