class Customer:
    def __init__(self, id,name,address):
        self.id = id
        self.Name = name
        self.Address = address


    def displayDetails(self):
        print("Name : " + self.Name)
        print("Address : " + self.Address)

    

    def registerCustomer(self):
        self.Name = input(" Enter Name :")
        self.Address = input("Enter Address :")
        

    