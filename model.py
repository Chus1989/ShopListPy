class ShoppingList:
    def __init__(self):
        self.items = []

    def getItem(self):
        return self.items

    def addItem(self, item):
        self.items.append(item)
        
    def removeItem(self,item):
        self.items.remove(item)