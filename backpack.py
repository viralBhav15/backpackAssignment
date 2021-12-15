
class Backpack:
    
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.items = []
        self.open = False
    
    def openBag(self):
        self.open = True
        print("The bag is currently open.")

    def closeBag(self):
        self.open = False
        print("The bag is now closed.")

    def putIn(self, item):
        if self.open == True:
            self.items.append(item)
            print(item + " has been placed in the bag.")
        else:
            print("The bag is currently closed.")

    def takeOut(self, item):
        if self.open == True and item in self.items:
            self.items.remove(item)
            print(item + " has been removed from the bag.")
        

backpack1 = Backpack("Blue", "Small")
backpack2 = Backpack("Red", "Medium")
backpack3 = Backpack("Green", "Large")

backpack2.openBag()
backpack2.putIn("Lunch")
backpack2.putIn("Jacket")
backpack2.closeBag()
backpack2.openBag()
backpack2.takeOut("Jacket")
backpack2.closeBag()