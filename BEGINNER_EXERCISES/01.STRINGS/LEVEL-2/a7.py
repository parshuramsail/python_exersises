# count repeated characters

s = 'lhelloel'
repeated_count = 0
repeated_chars = []
for char in s:
    if (s.count(char) > 1) and (char not in repeated_chars):
        repeated_count += 1
        repeated_chars.append(char)
print(repeated_chars)
print(repeated_count)
