import sqlite3


class DbConnect:
    def __init__(self):
            self._file1=sqlite3.connect("file30.db")
            self._file1.row_factory = sqlite3.Row
            self._file1.execute("create table if not exists Admin(ID integer primary key autoincrement,Name text,Age int)")
            self._file1.commit()

    def FileAdd(self,Name,Age):
        self._file1.row_factory = sqlite3.Row
        self._file1.execute("insert into Admin(Name,Age) values (?,?)", (Name,Age))
        self._file1.commit()
        print("record printed")

    def FileDelete(self,DBID):
        self._file1.row_factory = sqlite3.Row
        self._file1.execute("delete from Admin where ID={}".format(DBID))
        self._file1.commit()
        print("the desired entry has be deleted")

    def FileRead(self):
        self._file1.row_factory = sqlite3.Row
        InnerDataReaded = self._file1.execute("select * from Admin")
        for EachRow in InnerDataReaded:
            print(" ID:{}, Name: {}, Age: {}".format(EachRow["ID"], EachRow["Name"], EachRow["Age"]))
        self._file1.commit()

    def FileUpdate(self,DBID,Age):
        self._file1.row_factory = sqlite3.Row
        self._file1.execute("update Admin set Age=? where ID=?", (Age,DBID))
        self._file1.commit()
        print("your details updated")

