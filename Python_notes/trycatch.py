def main():
    try:
        file=open("test.txt","w")
        for line in file:
            print("line")
        file.close()
    except IOError:
        print("file not found")
        print(main2())

def main2():
    try:
        x=int(input("type your name"))
        return x
    except ValueError:
        print("user typed string instad of number")

if __name__ == '__main__':main()
