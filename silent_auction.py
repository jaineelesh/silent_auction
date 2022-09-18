import os

gavel_art = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
'''
print(gavel_art)
print("Welcome to the secret auction program.")
bids_db: dict[str, int] = {}


def add_bid(name, bid):
    """
    :type name: str
    :type bid: int
    """

    bids_db[name] = bid


def winner_bid():
    winner = ""
    bid = 0
    for n, b in bids_db.items():
        if b > bid:
            winner = n
            bid = b
    return (winner, bid)


while True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    add_bid(name, bid)
    if input("Are there any other bidders? Type 'y' to continue 'n' to stop: ") == 'y':
        pass
    else:
        break
    os.system("cls")

print(winner_bid())
