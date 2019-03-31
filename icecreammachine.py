"""
3. Ice Cream Machine - medium

Implement the IceCreamMachine's scoops method so that it returns all combinations of one ingredient and one topping. If there are no ingredients or toppings, the method should return an empty list.

For example,

IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"]).scoops()

should return

[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']].
"""
class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        combinations = []
        for topping in self.toppings:
            for ingredient in self.ingredients:
                combinations.append([ingredient, topping])
        return combinations

machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
print(machine.scoops())
#should print
# [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce","orange"])
print(machine.scoops())
# this should print
#[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce'], ['vanilla','orange'], ['chocolate','orange']]
