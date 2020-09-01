

class Car:
    def __init__(self,**kwargs):
        self._Data=kwargs
    def GetModel(self):
        return self._Data["company"]
    def GetPrice(self):
        return self._Data["price"]
    def GetMilesDriven(self):
        return self._Data["milesdriven"]
    def GetYear(self):
        return self._Data["year"]


def main():
    mycar=Car(company="BMW",price=2321222,milesdriven=456,year=2019)
    carprice=mycar.GetPrice()
    print("ram car price = {}".format(carprice))


    poojacar=Car(company="Ford",price=9999,milesdriven=56,year=2018)
    carprice=mycar.GetPrice()
    print("pooja car price = {}".format(carprice))

if __name__ == '__main__':main()



