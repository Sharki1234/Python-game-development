class Product:
    chocolate = 10
    banana = 2
    raspberry = 7
    maggi = 5
    orange = 8
    products =  [chocolate,banana,raspberry,maggi,orange]
    def check(self,name):
        for num in self.products:
            if num == name:
                return num

class Product2:
    objects = ["chocolate","banana","raspberry","maggi","orange"]
    price = [10,2,7,5,8]
    def find(self,name):
        num = self.objects.index(name)
        return(self.price[num])

        
    
    


class User:
    def __init__(self):
        self.cart = []
        self.cart2 = []
        useradd = input("what product do you want to add")
        b = Product2()
        price2 = b.find(useradd)
        self.cart2.append(price2)

begin = User()
print(begin.cart2)



