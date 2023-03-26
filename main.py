from food_operations import FoodFunctions
class Main:
    def execute(self,choice):
        if choice == 1:
            print ('********Food Id**********')
        if choice == 2:
            print ('********Food Name*********')
        if choice == 3:
            print ('******** Food Quantity*******')
        if choice == 4:
            print('********Food Price**********')
        if choice == 5:
             print('********Food Discount**********')
        if choice == 6:
             print('********Food stock**********')
        





main = Main
foodfunctions = foodfunctions()

choice = int(input('Enter\n1.Food Idn\2.Food name.n\3Food Quantity.n\4Food Price.n\5Food Discount.n\6Food Stock'))
main.execute(choice)
