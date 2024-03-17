import csv

class Item:
    all = []
    pay_rate = 0.8
    def __init__(self,name,price,quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
    def calculatePrice(self,quantities,discount:bool):
        return quantities*self.price * self.pay_rate if discount else quantities*self.price
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
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        if len(value) > 10:
            raise Exception("The name is too long")
        else:
            self.__name = value
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}','{self.price}','{self.quantity}')"