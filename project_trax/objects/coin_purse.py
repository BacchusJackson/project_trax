class CoinPurse():
    def __init__(self, coins=0, owner=None):
        self.coins = coins
        self.owner = None

    def mod_total(self, total):
        self.coins = total

    def add(self, coins):
        self.coins += coins

    def rm(self, coins):
        self.coins += coins

    def transfer_to(self, other_purse, coins):
        self.rm(coins)
        other_purse.add(coins)

    def transfer_from(self, other_purse, coins):
        other_purse.rm(coins)
        self.add(coins)