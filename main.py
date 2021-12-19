from restuarant import Restaurant


class Swiggy:
    def __init__(self):
        self.restaurants = {}

    #Restaurant methods ****************************************************************
    def addMenuItemToRestaurant(self, resId, name, price):
        if resId in self.restaurants:
            rest = self.restaurants[resId]
            rest.addMenuItems(name, price)
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

    # TODO:********************************************************************************


def main():
    s = Swiggy()
    i =1
    while i!=0:
        print("Choose Options (1/2/3/0): ")
        print("1) Create Restaurant.")
        print("2) Delete Restaurant.")
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
            tokens = input()
            s.deleteRestaurant(tokens)
        elif tokens[0] =='0':
             exit()
        else:
            print("ERROR - Unsupported instruction")
        #loop increment
        i=i+1



#for start system
main()

