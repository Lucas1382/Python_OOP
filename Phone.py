from Item import Item

class Phone(Item):
    def __init__(self,name,price,quantity,brokenPhone = 0):
        super().__init__(
            name,price,quantity
        )
        self.brokenPhone = brokenPhone