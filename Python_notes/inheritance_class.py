class Operations:
    def sum(self,n1,n2):
        return n1+n2
    def division(self,n1,n2):
        return n1/n2

class MultiOperations(Operations):
    def multply(self,n1,n2):
        return n1*n2



def main():
    MulOp=MultiOperations()
    print(MulOp.sum(10,20))
    print(MulOp.multply(20,32))


if __name__ == '__main__':main()

