print("Welcome to the love calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()

joined_name = lower_name1+lower_name2

T = joined_name.count("t")
R = joined_name.count("r")
U = joined_name.count("u")
E = joined_name.count("e")

L = joined_name.count("l")
O = joined_name.count("o")
V = joined_name.count("v")
E = joined_name.count("e")

total = (T+R+U+E)*10 + (L+O+V+E)

if total < 10 or  total> 90 :
    print(f"your score is {total}" , "you go together like coke and mentos")
elif total > 40 and total < 50:
    print(f"your score is {total}", "you are alright together")
else:
    print(f"your score is {total}")
