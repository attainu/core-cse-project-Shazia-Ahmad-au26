# Food Delivery App(Swiggy)

This project is intended to implement and demonstrate features offered by Swiggy. It's written in python and offers all functionalities through instruction set given via command line.

## Requirements

Swiggy food delivery system implementation

### Modules Used

We have used two modules which is mentioned below:
import time(this is used for day,time & date formate)
import uuid(it is used to generate random/unique id)

### Approach Used

This project is based on OOP'S concept

    Swiggy(class): In this class we have implemented different functionalities like on board Restaurant , manage restaurant  menu ,User  signup ,login & logout , search food, select food, get cart , place order , generate bill, payment, delivery status, customer feedback etc. 
    Restaurant(class): In this class we have implemented different functionalities like manage restaurants details, status(open/close), get menu, add menu items , update menu, delete menu .
    Foods (class): This class is created to capture food details currently there are only few required fields like name and price. But based on future requirements additional fields and functionalities can easily be added.
    Customer(class): In this class we have implemented some  functionalities like manage user details, accept delivery status, reject delivery status.
    Cart(class): In this class we have implemented some  functionalities like add food items, remove food items, modify quantity.
    Orders(class): In this class we have implemented some  functionalities like  print bill, mange orders details.

#### Instruction to run

This program are driven based on instruction set. It accepts number of test cases as first input and then ready that many times to get instruction from command line. It performs operations based on given instruction and print result on screen.
