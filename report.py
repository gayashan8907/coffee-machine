class Resources:
    def __init__(self,water,milk,coffee,money=0):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money
    def enough_resources(self,used_water,used_milk,used_coffee):
        if self.water<used_water:
            print("Sorry,Not enough water")
            return False


        elif self.milk<used_milk:
            print("Sorry,Not enough milk")
            return False

        elif self.coffee<used_coffee:
            print("Sorry,Not enough coffee")
            return False
        return True

    def print_report(self):
        print(f"water:{self.water}ml\nmilk:{self.milk}ml\ncoffee:{self.coffee}g\nmoney:{self.money}")

    def after_make(self,water1,milk1,coffee1,cost):
        self.water -= water1
        self.milk -= milk1
        self.coffee -= coffee1
        self.money += cost





