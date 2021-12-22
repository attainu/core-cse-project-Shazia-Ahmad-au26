class Customer:
    def __init__(self, userName,name,address,mobNo,password):
        self.Username = userName
        self.Name = name
        self.Address = address
        self.MobNo = mobNo
        self.password = password


    def displayDetails(self):
        print("Name : " + self.Name)
        print("Address : " + self.Address)

    

    

    