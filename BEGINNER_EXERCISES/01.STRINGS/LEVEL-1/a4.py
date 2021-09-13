# First and Last 3 characters of a string

# option-1
string = 'Wonderful'
if len(string) < 6:
    print('')
else:
    new_string = string[:3] + string[len(string)-3:]
    print(new_string)


# option-2
word = 'Amazing'
num_char = 3
if len(word) < num_char*2:
    print('')
else:
    answer = word[:num_char] + word[len(word)-num_char:]
    print(answer)
