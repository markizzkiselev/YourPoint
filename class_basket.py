class Basket:
    def __init__(self):
        self.basket = {}
        self.prices = {}
        self.height = 0

    def __len__(self):
        n = 0
        for i in self.basket:
            n += self.basket[i]
        return n

    def up(self, height=1):
        self.height += height

    def down(self, height=1):
        self.height -= height

    def get_height(self):
        return self.height

    def append(self, item, price=0):
        if item in self.basket:
            self.basket[item] += 1
        else:
            self.basket[item] = 1
            self.prices[item] = int(price)

    def get_price(self, item, col=1):
        return self.prices[item] * col

    def give_basket(self):
        return self.basket
