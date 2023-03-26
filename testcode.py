cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

card_num = 2
more_card = input("Type 'y' for more card or 'n' for pass: ")


def card_generator():
  global card_num
  if more_card == "y":
    card_num = card_num+1
    card_new = cards[:card_num]
    return card_new
  elif more_card == "n":
    card_new = cards[:card_num]
    return card_new

