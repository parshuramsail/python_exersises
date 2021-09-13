# Make a frequency dictionary from the elements of a list()

my_list = ['a', 'a', 'b', 'c', 'a', 'b']
frequency_dict = {}

for i in my_list:
    if i not in frequency_dict:
        frequency_dict[i] = 1
    else:
        frequency_dict[i] += 1
print(frequency_dict)
