import sqlite3

file1=sqlite3.connect("file30.db")

def FileCreation():
    file1.row_factory=sqlite3.Row
    file1.execute("create table if not exists Admin(ID integer primary key autoincrement,Name text,Age int)")
    file1.commit()

def FileAdd(Name,Age):
    file1.row_factory=sqlite3.Row
    file1.execute("insert into Admin(Name,Age) values (?,?)",(Name,Age))
    file1.commit()
    print("record printed")

def FileDelete(DBID):
    file1.row_factory=sqlite3.Row
    file1.execute("delete from Admin where ID={}".format(DBID))
    file1.commit()
    print("the desired entry has be deleted")
def FileRead():
    file1.row_factory=sqlite3.Row
    InnerDataReaded = file1.execute("select * from Admin")
    for EachRow in InnerDataReaded:
        print(" ID:{}, Name: {}, Age: {}".format(EachRow["ID"],EachRow["Name"],EachRow["Age"]))
    file1.commit()

def FileUpdate(DBID,Age):
    file1.row_factory=sqlite3.Row
    file1.execute("update Admin set Age=? where ID=?",(Age,DBID))
    file1.commit()
    print("your details updated")

# def FileProcess():
#     while 1:
#         try :
#             inputIO=int(input("\n=======\n"
#                             "\n 1 - add new entry"
#                             "\n 2 - check all the entries"
#                             "\n 3 - Update specific entrie"
#                             "\n 4 - delete entry"
#                             "\n 0 - exit "
#                             "\n=======\n"
#                             "enter you input : "))
#             if inputIO == 0:
#                 break;
#
#             elif inputIO == 1:
#                 Name = input("enter name")
#                 Age = int(input("enter your age "))
#                 FileAdd(Name,Age)
#
#             elif inputIO == 2:
#                 FileRead()
#
#             elif inputIO == 4:
#                 DBID = int(input("enter You Data Base ID"))
#                 FileDelete(DBID)
#
#             elif inputIO == 3:
#                 DBID = int(input("enter your Data Base ID "))
#                 Age = int(input("enter age to update"))
#                 FileUpdate(DBID,Age)
#         except ValueError:
#             print("enter number from the above menu")

def main():
    FileCreation()
    while 1:
        try :
            inputIO=int(input("\n=======\n"
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
                FileAdd(Name,Age)

            elif inputIO == 2:
                FileRead()

            elif inputIO == 4:
                DBID = int(input("enter You Data Base ID"))
                FileDelete(DBID)

            elif inputIO == 3:
                DBID = int(input("enter your Data Base ID "))
                Age = int(input("enter age to update"))
                FileUpdate(DBID,Age)
        except ValueError:
            print("enter number from the above menu")


if __name__ == '__main__':main()




