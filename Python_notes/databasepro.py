import sqlite3


# to open a data base on sql
hello=sqlite3.connect("world.db")

# to create a table in sql
def table1():
    # row creation
    hello.row_factory=sqlite3.Row
    #  creation of admin in the form of rows
    hello.execute("create table if not exists Admin(Name text,Age int)")
    hello.commit()

# to add a name in sql
def add(Name,Age):
    # add data in table
    hello.execute("insert into Admin(Name,Age) values(?,?)",(Name,Age))
    hello.commit()
    print("record added")

# to read the sql data base
def readadmin():
     # function to read admin
     dataread=hello.execute("select * from Admin")
     for rows in dataread:
         print("Name:{},Age:{}".format(rows["Name"],rows["Age"]))


# to delete some thing in the created data base
def delete(name):
    hello.execute("delete from Admin where Name='{}'".format(name))
    hello.commit()
    print("record is deleted")
# update the record function
def updatetable(Name,Age):
    hello.execute("update Admin set Age=? where Name=?",(Age,Name))
    hello.commit()
    print("record updated added")


def main():
    # create table with this function
    table1()
    # creating an input function
    # input1= int(input("number of entries, enter:"))
    while 1:
        input1 = int(input("\n==\n number of entries,"
                           "\n 1 - to add new name"
                           "\n 2 - to read the data base"
                           "\n 3 - to delete an entry in data base"
                           "\n 4 - to update record"
                           "\n 0 - Exit"
                           "\n=====\n"
                           "index number please : "))
        if input1 == 0:
            break;

        elif input1 == 1:
            Name = input("enter Name :")
            Age = int(input("enter Age"))
            add(Name, Age)

        elif input1 == 2:
            readadmin()

        elif input1 == 3:
            name = input(input("enter name to delete:"))
            delete(name)

        elif input1 == 4:
            Name = input("enter name")
            Age = int(input("enter age"))
            updatetable(Name,Age)


if __name__ == '__main__': main()
