class Customer:
    def __init__(self, userName,name,address,mobNo):
        self.Username = userName
        self.Name = name
        self.Address = address
        self.MobNo = mobNo


    def displayDetails(self):
        print("Name : " + self.Name)
        print("Address : " + self.Address)

    

    

    