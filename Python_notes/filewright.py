


def main():
    x=open("hello.txt","a")
    for i in range(5):
        inputtext=input("type text here")
        x.write("\n this is the name u printed {}".format(inputtext))

    x.close()


if __name__ == '__main__':main()
