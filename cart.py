class Product:
    objects = ["chocolate","banana","raspberry","maggi","orange"]
    price = [10,2,7,5,8]
    def find(self,name):
        num = self.objects.index(name)
        return(self.price[num])

        
class User:
    cart = []
    cartnames = []
    order_record = []
    order_pricerecord = []
    def add(self):
        x =0
        while x ==0:
            useradd = input("what product do you want to add")
            b = Product()
            price = b.find(useradd)
            self.cart.append(price)
            self.cartnames.append(useradd)
            more = input("do you want to add any more products?")
            if more == "yes":
                x = 0
            else:
                x = 1
       

    def view(self):
        
        view = input("do you want to view your products ").lower()
        if view == "yes":
            refined = ", ".join(self.cartnames)
            print(refined)
        else:
            print("go back to menu")
    def order(self):
        orders = 0
        place = input("are you ready to order?").lower()
        if place == "yes":
            orders += 1
            order_name = (f"order {orders}){len(self.cartnames)} items")
            order_price = (f"the total price is:£{sum(self.cart)}") 
            print(f"your order is:{refined} and {order_price}")
            self.order_pricerecord.append(order_price)
            self.order_record.append(order_name)
            cart = []
            cartnames = []
        else:
            print("go back to the menu")
        
    def view_orders(self):
        print(f"{''.join(self.order_record)} with {''.join(self.order_pricerecord)}")
        print()

    
    


while True:
    menu = input("what do you wnat to do?").lower()
    action = User()
    if menu == "add":
        action.add()
    elif menu == "check cart":
        action.view()
    elif menu == "view orders":
        action.view_orders()
    elif menu == "order":
        action.order()