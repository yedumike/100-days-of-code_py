#################<<<<<<<<< AUNCTION PROGRAM >>>>>>>>>>#######################

def check_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bidding_amount = bidding_dictionary[bidder]
        if bidding_amount > highest_bid:
            highest_bid =  bidding_amount
            winner = bidder
    print(f'Winner is {winner}')


continue_bidding = True

bids = {}
while continue_bidding:

    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if should_continue == "no":
        continue_bidding = False
        check_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)

