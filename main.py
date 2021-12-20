from restuarant import Restaurant
from customer import Customer


class Swiggy:
    def __init__(self):
        self.restaurants = {}
        self.customer = {}

    #Restaurant methods ****************************************************************
    def addMenuToRestaurant(self, resId,foodId, name, price):
        if resId in self.restaurants:
            rest = self.restaurants[resId]
            rest.addMenuItems(foodId,name, price)
        else:
            print("ERROR : Invalid restaurant Id")

    def addRestaurant(self, resId, name, address, mobileNum):
        res = Restaurant(resId, name, address, mobileNum)
        if resId not in self.restaurants:
            self.restaurants[resId] = res
        else:
            print("ERROR - Restaurant with same id already exists")

    def deleteRestaurant(self, resId):
        if resId  in self.restaurants: 
            self.restaurants.pop(resId)
        else:
            print("ERROR - Restaurant with same id not found")

    def displayRestaurants(self):
        self.addRestaurant("1","Chinese kitchen","Dwarka sector 7",'9650320227')
        self.addMenuToRestaurant("1","1","Noodles","90")
        self.addMenuToRestaurant("1","2","Momos","120")
        self.addRestaurant("2","South Vibes","uttam nagar","8506834632")
        self.addMenuToRestaurant("2","1","Sambhar","50")
        self.addRestaurant("3","Sweets Shop","Dabri Mor","987678953")
        self.addMenuToRestaurant("3","1","Gulab Jamun","220")
        print("ID   Restaurant's Name   Address")
        for key,value in self.restaurants.items():
            print(value.resId + "   " + value.ResName +"   "+value.Address)



    # TODO:********************************************************************************


    def selectItem(self,resId):
        rest = self.restaurants[resId]
        i=1
        while i!=0:
            rest.displayMenu()
            selectId = input(" select Food using IDs : ")

            i=i+1
        

    def signUp(self,userName,name,address,mobNum,):
        cus = Customer(userName,name,address, mobNum)
        if userName not in self.customer:
            self.customer[userName] = cus
            print("signUp Successfully")
            self.selectRestaurants()
        else:
            print("ERROR - username with same id already exists")

    def selectRestaurants(self):
        self.displayRestaurants()
        i = 1
        while i!=0:
            selectId = input(" select Restaurants using IDs : ")
            if selectId in self.restaurants:
                self.selectItem(selectId)
            elif selectId =="0":
                break
            
            i=i+1
            
            
    
    
             






     


def main():
    s = Swiggy()
    i =1

    def restaurantOwner():
        while i!=0:
            print("Choose Options (1/2/3/0): ")
            print("1) Create Restaurant.")
            print("2) Delete Restaurant.")
            print("3) Add Menu to restaurant")
            print("for exit please type 0")
            tokens = input("Enter Options : ").split("|")
            if (len(tokens[0]) <= 0):
                break
            elif tokens[0]=='1':
                id = input("enter ID : ")
                name = input("Enter Name : ")
                address = input("Enter Address : ")
                number = input("Enter Number : ")
                s.addRestaurant(id, name,address,number)
            elif tokens[0] == "2":
                print("Please enter id of the restaurant you want to delete.")
                s.deleteRestaurant(tokens)

            elif tokens[0] == "3":
                resId = input("Enter restaurant ID")
                foodId = input("Enter food ID")
                name = input("enter item Name")
                price = input("Enter Item's Price")
                s.addMenuToRestaurant(resId,foodId, name, price)
            elif tokens[0] =='0':
                exit()
            else:
                print("ERROR - Unsupported instruction")
            #loop increment
            i=i+1

    def customer():

        while i!=0:
            print("Choose Options (1/2/0): ")
            print("1)  sign Up.")
            print("2)  Login.")
            token = input("Enter option :")

            if token[0] =="1":
                userName = input("Enter user name :")
                name = input("Enter Your name :")
                address = input("Enter your address :")
                mobNum = input("Enter your mob number :")
                s.signUp(userName,name,address,mobNum)



                
            elif token[0]=="2":
                pass

            elif token[0]=="0":
                exit()        




        
            # In method (Main) 
    while i!=0:
        print("Choose Options (1/2/0): ")
        print("1) If customer")
        print("2) If Restaurant Owner.")
        token = input("Enter option :")

        if token[0]=="1":
            customer()
        elif token[0]=="2":
            restaurantOwner()

           



#for start system
main()

