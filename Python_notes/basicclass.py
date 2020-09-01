class user:
    def SetUser(self,username):
        self._User = username
    def GetUser(self):
        return self._User

def main():
    user1=user()
    user1.SetUser("ramteja")
    print(user1.GetUser())
    user2=user()
    user2.SetUser("pooja")
    print(user2.GetUser())


if __name__ == '__main__':main()
