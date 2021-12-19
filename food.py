class Food :

    def __init__(self,name,price=None,quantity=0):
        self.Name = name
        self.Price= price

    def getPrice(self):
        return self.Price

    def __str__(self):
        return self.Name + ' , Price: ' + str(self.getPrice())
