#!/usr/bin/python3
output = ""
for letter in range(ord('a'), ord('z') + 1):
    output += chr(letter)
print("{}".format(output), end="")
