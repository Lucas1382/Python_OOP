from Item import Item

class Phone(Item):
    pay_rate = 0.5
    def __init__(self,name,price,quantity,brokenPhone = 0):
        super().__init__(
            name,price,quantity
        )
        self.brokenPhone = brokenPhone