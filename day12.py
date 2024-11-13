#Password Generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols= ["!","#","$","%","&","(",")","*","+"]

print("Welcome to the password generator")
nr_letters = int(input("How many letters would you like in your password? (Enter a number)\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#easy level
# password = ""
# for char in range(0,nr_letters):
#     password += random.choice(letters)

# for sym in range(0,nr_symbols):
#     password += random.choice(symbols)

# for numb in range(0,nr_numbers):
#     password += random.choice(numbers)

# print(f"Your password is: {password}")



password = []
for char in range(0,nr_letters):
    password.append(random.choice(letters))

for sym in range(0,nr_symbols):
    password.append(random.choice(symbols))

for numb in range(0,nr_numbers):
    password.append(random.choice(numbers))


print(f"Your password is: {password}")
random.shuffle(password)
print(f"Shuffled password is: {password}")
final_pass = ""
for char in password:
    final_pass += char

print(f"final password: {final_pass}")