MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}
# for value in MENU["espresso"]["ingredients"].values():
#    print(value)
choice = input("What would you like? (espresso/latte/cappucino): ")
# print(MENU[choice]["ingredients"].get("water"))

# print(MENU["espresso"]["ingredients"].values() > resources.values())
for u, v in resources.items():
    print(u, v)
for u, v in MENU[choice]["ingredients"].items():
    print(u, v)
