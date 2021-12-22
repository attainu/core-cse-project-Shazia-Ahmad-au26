from food import Food

class Cart:
    def __init__(self, cartid):
        self.cartId = cartid
        self.resId = None
        self.items = []
        self.cartData = {}
        self.count = {}
        self.totalQuantity =0
        self.sumAmount = 0

    def addFoodItems(self, foodId,foodObject):
        if foodId not in self.cartData:
            self.cartData[foodId] =foodObject 
            self.items.append(self.cartData)
            self.count[foodId] = 1
            print("INFO : Food item id {} added to your cart"
                .format(foodId))
        elif foodId in self.cartData:
                self.count[foodId] += 1
                print("INFO : Food item id {} is updated to your cart"
                    .format(foodId))


    def getTotalAmount(self):
        sum=0
        for key,value in self.cartData.items():
            for countKey,countValue in self.count.items():
                if key==countKey:
                    for i in range(0,countValue):
                        sum += int(value.getPrice())
        self.sumAmount = sum
        return self.sumAmount
                    

    def getItemQuantity(self):
        quantity =0
        for key,value in self.cartData.items():
            for countKey,countValue in self.count.items():
                if key==countKey:
                    for i in range(0,countValue):
                        quantity +=1

        self.totalQuantity = quantity
        return self.totalQuantity





    def removeFoodItems(self, food):
        missing = True
        for i in range(len(self.foods)):
            if self.foods[i].name == food:
                self.items.pop(i)
                self.items.quantities(i)
                missing = False
                print("INFO : Food Item {} removed from your cart[{}]"
                      .format(food, self.cartId))
        if missing:
            print("ERROR : This food item [{}] is not in your cart[{}]"
                  .format(food, self.cartId))

    def modifiyQuantity(self, qty, food):
        missing = True
        for i in range(len(self.items)):
            if food.name == self.foods[i].name:
                self.quantities[i] = qty
                missing = False
                print("INFO : Food quantity updated successfully in cart")
        if missing:
            print("ERROR : This food item [{}] is not in your cart[{}]"
                  .format(food, self.cartId))


    def displayCartItems(self):
        for key,value in self.cartData.items():
            itemCount = 0
            for countKey,countValue in self.count.items():
                    if key==countKey:
                        for i in range(0,countValue):
                            itemCount+=1
            print(f"{itemCount} items of {value.Name}")
        print("Total Items in cart is : ",self.getItemQuantity())
        print("Total Price is : ",self.getTotalAmount(),"Rs")

