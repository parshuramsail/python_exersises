# Remove nth character from a string

# option-1
s = 'hello'
n = 1

if (len(s) == 0) or (n >= len(s)):
    print('')
else:
    new_s = ""
    for i in range(len(s)):
        if i != n:
            new_s += s[i]
    print(new_s)

# option-2
s = 'hello'
n = 1

if (not(s)) or (n >= len(s)):
    print('')
else:
    new_s = ""
    for i in range(len(s)):
        if i != n:
            new_s += s[i]
    print(new_s)
