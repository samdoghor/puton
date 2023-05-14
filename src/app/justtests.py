class Tests:
    """"""

    def __init__(self):
        self.target = None
        self.game_odd = None

    def target_input(self):
        self.target = int(input("Enter your target: "))

    def game_odd_input(self):
        self.game_odd = float(input("Enter the game odd: "))

    def stake(self):
        self.stake = self.target/((self.game_odd) - 1)
        return self.stake


# create an instance of the Values class
values = Tests()

# prompt the user for input
values.target_input()
values.game_odd_input()

# calculate the stake
stake = values.stake()
print(f"Stake: {stake}")
