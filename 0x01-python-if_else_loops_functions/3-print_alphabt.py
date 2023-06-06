#!/usr/bin/python3
output = ""
for letter in range(ord('a'), ord('z') + 1):
    if chr(letter) not in ['q', 'e']:
        output += chr(letter)
print("{}".format(output), end="")
