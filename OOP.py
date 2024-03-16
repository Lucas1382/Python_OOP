class Item:
    all = []
    pay_rate = 0.8
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
    def calculatePrice(self,quantities,discount):
        return quantities*self.price * Item.pay_rate if discount else quantities*self.price
    def __repr__(self) -> str:
        return self.name
    
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 6)
# This is for test PULL in Git. The Pull is success so i will push it again
print(Item.all)
