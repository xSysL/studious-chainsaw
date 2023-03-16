logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)


print("Welcome to Secret bidding auction")

bids = {}
bidding_finished = False

def highest_bidder(bidders):
  max_bidding_amount = 0
  winner = ''
  for bidder in bidders :
    bidder_amount = bidders[bidder]
    if bidder_amount > max_bidding_amount :
      max_bidding_amount = bidder_amount
      winner = bidder
  print(f'The winner is {winner} with a bidding amount of {max_bidding_amount}')

while not bidding_finished:
  name = input("Enter your name: ")
  bid = int(input("Enter your bidding amount: "))
  bids[name] = bid
  should_continue = input("More bidder? Type yes or no: ")
  if should_continue == 'no':
    bidding_finished = True
    highest_bidder(bids)
  elif should_continue == 'yes':
    #clear()
    print("Glitch")