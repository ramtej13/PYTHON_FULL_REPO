import sqlite3



def main():

    hello= sqlite3.connect("hello.db")
    hello.row_factory=sqlite3.Row
    hello.execute("create table if not exists Admin(Name text,Age int)")

    #add records
    hello.execute("insert into Admin(Name,Age) values(?,?)",("hussein",28))
    hello.commit()


if __name__ == '__main__':main()







