import datetime

def main():
    print("hello")
    dob = input("enter you age here ")
    currentYear = datetime.datetime.now().year - int(dob)
    age = "you age is {}".format(currentYear)
    print(age)
    print("hello world")

if __name__ == '__main__':main()
