#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = str(number)[-1]
sign = "-" if number < 0 else ""
print("Last digit of", number, "is", sign + str(last_digit), end=" ")
if int(sign + str(last_digit)) > 5:
    print("and is greater than 5")
elif int(sign + str(last_digit)) == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
