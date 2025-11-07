class A:
    def __init__(self,xterm,constant):
        self.a = xterm
        self.b = constant
    def __str__(self):
        return(f"{self.a}x + {self.b}")
    def __add__(self,other):
        return A(self.a + other.a,self.b+other.b)

o1 = A(-3,9)
o2 = A(4,5)
print(o1+o2)