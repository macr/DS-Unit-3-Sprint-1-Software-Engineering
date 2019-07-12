from random import randint


class Product:

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        stealability = self.price/self.weight
        if stealability >= 1.0:
            return 'Very stealable!'
        if stealability >= 0.5:
            return 'Kinda stealable.'
        return 'Not so stealable...'

    def explode(self):
        explosiveness = self.weight*self.flammability
        if explosiveness >= 50:
            return '...BABOOM!!'
        if explosiveness >= 10:
            return '...boom!'
        return '...fizzle.'


class BoxingGlove(Product):

    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight >= 15:
            return 'OUCH!'
        if self.weight >= 5:
            return 'Hey that hurt!'
        return 'That tickles.'
