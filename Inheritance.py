import csv

class Item:
    all = []
    pay_rate = 0.8
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
    def calculatePrice(self,quantities,discount:bool):
        return quantities*self.price * Item.pay_rate if discount else quantities*self.price
    @classmethod
    def instantiate_from_CSV(cls):
        with open('items.csv', 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)
        for item in items:
            Item(
                item.get('name'),
                float(item.get('price')),
                float(item.get('quantity'))
            )
    @staticmethod
    def is_integer(nums):
        if isinstance(nums,float):
            return nums.is_integer()
        elif isinstance(nums,int):
            return True
        else:
            return False
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}','{self.price}','{self.quantity}')"
    
class Phone(Item):
    def __init__(self,name,price,quantity,brokenPhone = 0):
        super().__init__(
            name,price,quantity
        )
        self.brokenPhone = brokenPhone
        
Item.instantiate_from_CSV()
Phone1 = Phone("Iphone",500,4,0)
print(Phone1.calculatePrice(2,1))
print(Item.all)