from admin_operation import Admin_operations
from user_operation import User_operations
class main_class:

    def _init_(self):
        self.Admin_operations = Admin_operations()
        self.User_operations = User_operations()

    def execute(self,first_choice):
        if first_choice==1:
            self.Admin_operations.admin_login()
        elif first_choice==2:
            self.User_operations.user_registration()
        else:
            print("Please enter correct option")
            print(f"{3-count} attempts left")


if "_name_" == "_main_":
    obj = main_class()
    count=1
    while count<=3: # main class has been provided 3 attempts to choose correct option, if his 3 attempts fail, after that it will stop.
        first_choice = int(input("Enter \n1.Admin \n2.User \nPlease Enter : "))
        obj.execute(first_choice)
        count+=1