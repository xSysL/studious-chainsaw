import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
letters_iter = int(input("How many letters do you want? \n"))
symbols_iter = int(input("How many symbols do you want? \n"))
numbers_iter = int(input("How many numbers do you want? \n"))

password = []
for i in range(0, letters_iter):
    i = random.choice(letters)
    password.append(i)

for i in range(0, symbols_iter):
    i = random.choice(symbols)
    password.append(i)

for i in range(0, numbers_iter):
    i = random.choice(numbers)
    password.append(i)

random.shuffle(password)

output = "".join(password)

print(f"Here is your password : {output}")

input("Press ENTER key to exit")
