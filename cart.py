class Product:
    objects = ["chocolate","banana","raspberry","maggi","orange"]
    price = [10,2,7,5,8]
    def find(self,name):
        num = self.objects.index(name)
        return(self.price[num])

        
class User:
    cart = []
    cartnames = []
    def add(self):
        useradd = input("what product do you want to add")
        b = Product()
        price = b.find(useradd)
        self.cart.append(price)
        self.cartnames.append(useradd)
    def view(self):
        orders = 0
        order_record = []
        view = input("do you want to view your products ").lower()
        if view == "yes":
            print(" ".join(self.cartnames))
            place = input("are you ready to order?").lower()
            if place == "yes":
                orders += 1
                order_name = (f"order {orders}){len(user.cartnames)} items")
                order_record.append(order_name)
            else:
                print("go back to the menu")
        else:
            print("go back to menu")

    
    
        
class Orders:
    def view_orders(self):
        x = Cart()
        print(''.join(x.order_record))

while True:
    menu = input("what do you wnat to do?").lower()
    action = User()
    if menu == "add":
        action.add()
    elif menu == "check cart":
        action.view()
    elif menu == "orders":
        action = Orders()