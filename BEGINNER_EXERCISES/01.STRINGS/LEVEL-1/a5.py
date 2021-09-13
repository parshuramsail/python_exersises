# Remove characters at even indieces

# option-1
string = 'hello'
new_string = ""

for i in range(len(string)):
    if i % 2 != 0:
        new_string += string[i]
print(new_string)

# option-2
string = 'hello'
new_string = ""

for i in range(1, len(string), 2):
    new_string += string[i]
print(new_string)
