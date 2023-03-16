card = [ 11, 1]

if sum(card) > 11 and 11 in card :
    card = [1 if item == 11 else item for item in card]

print(card)