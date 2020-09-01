
class Car:
    def SetModel(self,carmodel):
        self._Model=carmodel
    def SetPrice(self, carprice):
        self._Price = carprice
    def SetMilesDriven(self,totalmiles):
        self._MilesDriven= totalmiles
    def SetYear(self,purchasedyear):
        self._Year=purchasedyear
    def GetModel(self):
        return self._Model
    def GetPrice(self):
        return self._Price
    def GetMilesDriven(self):
        return self._MilesDriven
    def GetYear(self):
        return self._Year

def main():
    model=Car()
    model.SetModel("BMW")
    price=Car()
    price.SetPrice(2321222)
    milesdriven=Car()
    milesdriven.SetMilesDriven(456)
    year=Car()
    year.SetYear(2015)
    print(price.GetPrice())
    print(model.GetModel())

    Rammodel=Car()
    Rammodel.SetModel("gm")
    Ramprice=Car()
    Ramprice.SetPrice(99222)
    Rammilesdriven=Car()
    Rammilesdriven.SetMilesDriven(56)
    Ramyear=Car()
    Ramyear.SetYear(2000)
    print(Ramprice.GetPrice())
    print(Rammodel.GetModel())

if __name__ == '__main__':main()























