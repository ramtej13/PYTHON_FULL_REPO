
x=20
def main():
    # x=10
    print("x = {}".format(x))
    main1()

def main1():
    global x
    print(x)

if __name__ == '__main__':main()
