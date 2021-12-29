import os

print("Welcome to the secret auction program.\n")

other_bidders = True
auction = {}
hold_value = 0
winner = ""

def add_bidder(name, cash):
    auction[name] = cash

while other_bidders:
    name = input("What is your name?\n")
    cash = int(input("What's your bid?: $"))
    add_bidder(name, cash)
    others = input("Are there any other bidders? Type 'yes' or 'no.\n")
    if others == "no":
    #Alpha: 17, Beta: 21, Gamma: 13, Delta: 18
        for name in auction:
            if auction[name] > hold_value:
                hold_value = auction[name]
                winner = name
        print(f"The auction is won by {winner}. The final price is ${hold_value}.")
        other_bidders = False
    elif others == "yes":
        os.system("clear")
        continue