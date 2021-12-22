from restuarant import Restaurant
from customer import Customer
from cart import Cart
import time
from order import Order

class Swiggy:
    def __init__(self):
        self.restaurants = {}
        self.customer = {}
        self.carts = {}
        self.orders = {}
        self.pay = {}
        self.odHistory = {}
        self.currentUser = None
        self.autoGenrateRestaurants = False

    #**********************************************

    # define the countdown func.
    def countdown(self,t):
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print("      Please wait : "+timer, end="\r")
            time.sleep(1)
            t -= 1


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
        if self.autoGenrateRestaurants is False:
            #1st restaurant
            self.addRestaurant("1","Chinese kitchen","Dwarka sector 7",'9650320227')
            self.addMenuToRestaurant("1","1","Noodles","90")
            self.addMenuToRestaurant("1","2","Momos","120")
            self.addMenuToRestaurant("1","3","Egg Chowmein","70")
            self.addMenuToRestaurant("1","4","Hakka Noodles","90")
            self.addMenuToRestaurant("1","5","Fried Rice","80")
            #2nd restaurant
            self.addRestaurant("2","South Vibes","uttam nagar","8506834632")
            self.addMenuToRestaurant("2","1","Sambhar","50")
            self.addMenuToRestaurant("2","2","Rava dosa","60")
            self.addMenuToRestaurant("2","3","Upma","40")
            self.addMenuToRestaurant("2","4","Rice Idli","50")
            self.addMenuToRestaurant("2","5","Uttappam","80")
            #3rd restaurant
            self.addRestaurant("3","Sweets Shop","Dabri Mor","987678953")
            self.addMenuToRestaurant("3","1","Gulab Jamun","220")
            self.addMenuToRestaurant("3","2","Kaju Katli","420")
            self.addMenuToRestaurant("3","3","Rasagola","230")
            self.addMenuToRestaurant("3","4","Soan Papadi","110")
            self.addMenuToRestaurant("3","5","Peda","400")
            self.autoGenrateRestaurants = True
        print("ID   Restaurant's Name   Address")
        for key,value in self.restaurants.items():
            print(value.resId + "   " + value.ResName +"   "+value.Address)



    # TODO:********************************************************************************

    def selectFood(self, cartId, foodId,foodObject,resId):
        cart = self.getCart(cartId)
        cart.resId = resId
        cart.addFoodItems(foodId,foodObject)
        self.countdown(3)
        return cart

    def getCart(self, cartid):
        if cartid in self.carts:
            return self.carts[cartid]
        else:
            cart = Cart(cartid)
            self.carts[cartid] = cart
            return cart
    
    
    
    def selectItem(self,resId):
        rest = self.restaurants[resId]
        i=1
        print(rest.ResName + "'s Menu")
        while i!=0:
            rest.displayMenu()
            print("press 0 to back to restaurants.")
            selectId = input("select Food using IDs(1/2/3/4..) it will add to your cart : ")
            if selectId in rest.menu:
                    foodObj =  rest.menu[selectId]
                    self.selectFood(self.currentUser,selectId,foodObj,resId)
            elif selectId == '0':
                break
            i=i+1
        
    def cartItems(self):
        i=1
        while i!=0:
            cart = self.getCart(self.currentUser)
            print(f"{self.currentUser.Name}'s Carts *****************************")
            cart.displayCartItems()
            print("press 1 to place order.")
            print("press 0 to back to restaurants.")
            if len(self.carts)==0:
                print("your cart is empty please go back to restaurants and add food to your cart.")
            inp = input("Enter options : ")
            if inp =='1':
                self.countdown(2)
                print("************************************************************")
                if self.placeOrder():
                    self.countdown(3)
                    break
            elif inp =='0':
                break
            i+=1

    def deliverOrder(self, odId):
        if odId in self.orders:
            order = self.orders[odId]
            order.payStatus = "Delivered"
            print("delivered succesfully!")
        else:
            print("Invalid Id!")


    def signUp(self,userName,name,address,mobNum,password):
        cus = Customer(userName,name,address, mobNum,password)
        if userName not in self.customer:
            self.customer[userName] = cus
            self.currentUser = cus
            print("signUp Successfully")
            self.countdown(3)
            self.selectRestaurants()
        else:
            print("ERROR - username with same id already exists")

    def selectRestaurants(self):
        i = 1
        while i!=0:
            self.displayRestaurants()
            print("press 4 to go to Cart")
            selectId = input(" select Restaurants using IDs : ")
            if selectId in self.restaurants:
                self.selectItem(selectId)
            elif selectId == '4':
                self.cartItems()
            elif selectId =="0":
                break
            
            i=i+1

        
    def logIn(self, userName, password):
        if userName not in self.customer:
            print("Please signup")
            self.countdown(3)
        else:
            user = self.customer[userName]
            if user.password == password:
                self.currentUser = user
                print("login successfully, Welcome {}!".format(user.Name))
                self.countdown(3)
                self.selectRestaurants()
            else:
                print("password is not matching!")

    def logOut(self):
        print("Logout successful, Good Bye {}".format(self.currentUser.Name))
        self.currentUser = None
            
            
    def placeOrder(self):
        isPlaced = False
        if self.currentUser is None:
            print("Please login to place order")
            return
        cart = self.getCart(self.currentUser)
        order = Order()
        inp = input(f"Please Enter the amount {cart.sumAmount}Rs to place the order :")
        if int(inp)==cart.sumAmount:
            order.mobileNum = self.currentUser.MobNo
            order.payStatus="PAID"
            order.odrStatus="ACCEPTED"
            order.cartData = cart.cartData
            order.count = cart.count
            order.resId = cart.resId

            order.userName = self.currentUser.Name
            order.cartId = self.currentUser
            order.totalQuantity = cart.getItemQuantity()
            order.totalAmount = cart.getTotalAmount()

            self.orders[order.odId] = order
            order.displayOrder()
            print("Order created successfull!")
            isPlaced = True
            self.countdown(5)
            self.carts.clear()
            return isPlaced
        else:
            print("Order failed, all prodts not avlbl in a restaurant(s)")
        return isPlaced

    
#=======================================================================================================


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
                password = input("Enter password :")
                s.signUp(userName,name,address,mobNum,password)                
            elif token[0]=="2":
                userName = input("Enter user name :")
                password = input("Enter password :")
                s.logIn(userName,password)

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

           



#for start app
main()

