from food import  Food
from cart import Cart

class Restaurant():

    def __init__(self,resId,resName,address,mobilenum):
        self.resId = resId
        self.ResName= resName
        self.Address = address
        self.MobileNum= mobilenum
        self.menu= {}
        self.open = True
        
        

    # Input Methods ************************************************************************************************

    def addMenuItems(self,foodId,name, price):
        food = Food(foodId,name, price)
        if foodId not in self.menu:
            self.menu[foodId] = food
           # print("INFO : Menu item successfully added")
        else:
            print("ERROR : Menu item already added")


    def updateMenu(self,foodId,name, price):
        food = self.menu[foodId]
        if foodId is not None:
            food.price = price
            self.menu[foodId] = food
        else :
            print("ERROR : Menu item not found")

    def deleteMenu(self,foodId):
        self.menu.pop(foodId)


    # Display methods **************************************************************************************************
    
    def isOpen(self):
        return self.open


    def restaurantDetails(self):
        print("Restraunt Id :",self.resId)
        print("Restaurant Name :",self.ResName)
        print("Restaurant's Address :",self.Address)
        print("Restaurant's Number :",self.MobileNum)



    def displayMenu(self):
        for key,value in self.menu.items():
                print(value)
    
        


# res = Restaurant(1,"Raju Dhabha","JanakPuri",9990797860)

# res.restaurantDetails()

# res.addMenuItems("biryani",220)
# res.addMenuItems("chicken korma", 440)
# res.addMenuItems("Mutton Nihari", 620)
# res.addMenuItems("Mutton karori kawab", 220)
# res.addMenuItems("keema Pakode", 350)
# res.displayMenu()



    

