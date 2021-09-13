# Generate all Permutations of a list()
import itertools

my_list = [1, 2, 3]
permute = list(itertools.permutations(my_list))

for i in permute:
    print(list(i))  # for list
