class FourCal:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def setdata(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b

class MoreFourCal(FourCal):
    def pow(self):
        return self.a ** self.b

a = MoreFourCal(3,4)
print(a.add())
print(a.sub())
print(a.div())
print(a.mul())
print(a.pow())