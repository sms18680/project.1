
from food import Food_order

class FoodFunctions:
    foodlist = []

    def addFood(self):
        FoodId = int(input('enter your FoodId'))
        Name = input('enter food Name')
        Quantity = int('enter food Quantity')
        Price = float('enter food price')
        Discount = int(input('enter all discount'))
        Stock = int('enter food stock')
        food_obj = Food_order(FoodId,Name,Quantity,Price,Discount,Stock)
        self.foodlist.append(food_obj)
        print('Food Successfully Added!:')

