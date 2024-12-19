
'''
JESUS JOYAS 2024 shopping list
This class creates a instance of a product ith the parameters needed to operate with it
return tostring
'''

class ModelProduct:
    '''
    This is the init of the class and recives the paramenters
    args:
        id:String: The id of the product
        productName:String: the name of product
        purchased:Bool: if the product is purchased
        number:Int: The number to purchase

    '''
    def __init__ (self,id,productName, purchased,number):
        self.id = id
        self.name = productName
        self.purchased = purchased
        self.number = number

    def __repr__(self):
        return f"The product name is {self.name} and the quantity is : {self.number} and is purchsed = {self.purchased}/n"