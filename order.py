import time
import uuid


class Order:
    def __init__(self):
        self.odId = str(uuid.uuid1()).split("-")[0]
        self.resId = None
        self.cartId = None
        self.cartData = {}
        self.count = {}
        self.totalQuantity =0
        self.totalAmount = None
        self.payStatus = None
        self.odrStatus = None
        self.comment = None
        self.mobileNum = None
        self.userName = None
        self.time = time.asctime(time.localtime(time.time()))

    def displayOrder(self):
        print("Date of Order is : ",self.time)
        print("Order Id is : ",self.odId)
        for key,value in self.cartData.items():
            itemCount = 0
            for countKey,countValue in self.count.items():
                    if key==countKey:
                        for i in range(0,countValue):
                            itemCount+=1
            print(f"{itemCount} items of {value.Name}")
        print("Order is : ",self.odrStatus)
        print("Payment is : ",self.payStatus)
        print("Total Items in Order is : ",self.totalQuantity)
        print("Total Price is : ",self.totalAmount,"Rs")

