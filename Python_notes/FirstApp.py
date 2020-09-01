import datetime

dob = 1997
currentYear = datetime.datetime.now().year - dob
age = "dob-currentYear=age that is {}".format(currentYear)
print(age)
print("hello world")

print(datetime.datetime.now().time())


