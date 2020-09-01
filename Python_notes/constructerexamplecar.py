
class Car:
    def __init__(self,carmodel,carprice,totalmiles,purchasedyear):
        self._Model=carmodel
        self._Price = carprice
        self._MilesDriven= totalmiles
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
    mycar=Car("BMW",2321222,456,2015)
    carprice=mycar.GetPrice()
    print("ram car price = {}".format(carprice))


    poojacar=Car("Ford",9999,56,2018)
    carprice=mycar.GetPrice()
    print("pooja car price = {}".format(carprice))

if __name__ == '__main__':main()