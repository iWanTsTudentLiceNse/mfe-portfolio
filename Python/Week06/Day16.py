class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first*self.second

    def div(self):
        return self.first/self.second

a = FourCal()
a.setdata(4,2)

print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

class MoreFourCal(FourCal):
    def pow(self):
        return self.first**self.second

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first/self.second


b = MoreFourCal()
b.setdata(3,2)
print(b.add())
print(b.pow())