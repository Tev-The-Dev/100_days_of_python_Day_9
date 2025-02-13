import art
bidding_record = {}

print(art.logo)

def find_highest_bidder(bids):
    print('\n' * 20)
    for name, bid in bidding_record.items():
        if bid == max(bidding_record.values()):
            print(f"The winner is {name} with a bid of ${bid}")

bidding = True
while bidding:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidding_record[name] = bid
    others = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if others == 'no':
        find_highest_bidder(bidding_record)
        bidding = False
    elif others != 'yes' and others != 'no':
        print("That is not a valid option. Try again")
    else:
        print('\n'*20)