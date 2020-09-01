import sqlite3

from class_dbconnect import DbConnect
def main():
    Hello=DbConnect()
    while 1:
         try:
            inputIO = int(input("\n=======\n"
                                "\n 1 - add new entry"
                                "\n 2 - check all the entries"
                                "\n 3 - Update specific entrie"
                                "\n 4 - delete entry"
                                "\n 0 - exit "
                                "\n=======\n"
                                "enter you input : "))
            if inputIO == 0:
                break;

            elif inputIO == 1:
                Name = input("enter name")
                Age = int(input("enter your age "))
                Hello.FileAdd(Name, Age)

            elif inputIO == 2:
                Hello.FileRead()

            elif inputIO == 4:
                DBID = int(input("enter You Data Base ID"))
                Hello.FileDelete(DBID)

            elif inputIO == 3:
                DBID = int(input("enter your Data Base ID "))
                Age = int(input("enter age to update"))
                Hello.FileUpdate(DBID,Age)
         except ValueError:
             print("enter number from the above menu")

if __name__ == '__main__':main()
