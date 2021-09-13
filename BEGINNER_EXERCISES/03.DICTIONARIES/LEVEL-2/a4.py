# Make a frequency dictionary of the characers in the string
my_string = "Hello world"

frequency = {}

for value in my_string.lower():
    if value.isalpha():
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1
print(frequency)
