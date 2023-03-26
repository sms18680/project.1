# You have to design a Food Ordering app for a restaurant
# The application will have a log-in for admin and users to log-in
# -------------------------------- Admin ----------------------------------

# ➡️ Admin will have the following functionalities: ⬅️

# 👉 1. Add new food items. Food Item will have the following details:
#         🔴 FoodID //It should be generated automatically by the application.
#         🔴 Name
#         🔴 Quantity. For eg, 100ml, 250gm, 4pieces etc
#         🔴 Price
#         🔴 Discount
#         🔴 Stock. Amount left in stock in the restaurant.

# 👉 2. Edit food items using FoodID.

# 👉 3. View the list of all food items.

# 👉 4. Remove a food item from the menu using FoodID.
# --------------------------------- User ----------------------------------

# ➡️ The user will have the following functionalities: ⬅️

# 👉 1. Register on the application. Following to be entered for registration:
#         🔴 Full Name
#         🔴 Phone Number
#         🔴 Email
#         🔴 Address
#         🔴 Password

# 👉 2. Log in to the application

# 👉 3. The user will see 3 options:
#         🔴 Place New Order
#         🔴 Order History
#         🔴 Update Profile

# 👉 4. Place New Order: The user can place a new order at the restaurant.
#         🔵 Show list of food. The list item should as follows:
#             🔴 Tandoori Chicken (4 pieces) [INR 240]
#             🔴 Vegan Burger (1 Piece) [INR 320]
#             🔴 Truffle Cake (500gm) [INR 900]

# 👉 5. Users should be able to select food by entering an array of numbers. For example, if the user wants to order Vegan Burger and Truffle Cake they should enter [2, 3]

# 👉 6. Once the items are selected user should see the list of all the items selected. The user will also get an option to place an order.

# 👉 7. Order History should show a list of all the previous orders

# 👉 8. Update Profile: the user should be able to update their profile.

class Food_order:
    def __init__(self,FoodId,Name,Quantity,Price,Discount,Stock):
        self.FoodId =FoodId
        self.Name = Name
        self.Quantity = Quantity
        self.Price = Price
        self.Discount = Discount
        self,Stock = Stock
    def set_FoodId(self,FoodId):
        self.FoodId = FoodId
    def get_FoodId(self):
        return self.FoodId
    def set_Name(self,Name):
        self.Name = Name
    def get_Name(self):
        return self.Name
    def set_Quantity(self,Quantity):
        self.Quantity = Quantity
    def get_Quantity(self):
        return self.Quantity
    def set_Price(self,Price):
        self.Price = Price
    def get_Price(self):
        return self.price
    def set_Discount(self,Discount):
        self.Discount = Discount
    def get_Discount(self):
        return self.Discount
    def set_Stock(self,Stock):
        self.Stock = Stock
    def get_FoodId(self):
        return self.Stock