class Food :

    def __init__(self,id,name,price=None,quantity=0):
        self.id =id
        self.Name = name
        self.Price= price

    def getPrice(self):
        return self.Price

    def getId(self):
        return self.id





    def __str__(self):
        return  self.id + " "+self.Name + ' , Price: ' + str(self.getPrice())
