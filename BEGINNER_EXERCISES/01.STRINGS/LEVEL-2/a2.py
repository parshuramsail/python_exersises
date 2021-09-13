# String contaions all letters in Alphabet

# option->1
import string

s = "The quick brown fox jumps over the lazy dog"

set_s = set(s.lower())
set_s.remove(" ")  # remove sapces from the set

print(set_s == set(string.ascii_lowercase))


# option->2

s = "The quick brown fox jumps over the lazy dog"
is_panagram = True

for char in string.ascii_lowercase:
    if char not in s.lower():
        is_panagram = False
print(is_panagram)


# option->3

s = "The quick brown fox jumps over the lazy dog"
is_panagram = True

for char in string.ascii_lowercase:
    if char not in s.lower():
        is_panagram = False
        break
print(is_panagram)
