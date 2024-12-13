


class ModelProduct:
    def __init__ (self,id,productName, purchased,number):
        self.id = id
        self.name = productName
        self.purchased = purchased
        self.number = number

    def __repr__(self):
        return f"The product name is {self.name} and the quantity is : {self.number} and is purchsed = {self.purchased}"