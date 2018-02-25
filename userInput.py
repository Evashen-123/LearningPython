import datetime

name=input("what is your name?")
dob=int(input("what is your year of birth?"))
years=datetime.datetime.now().year-dob
print(name+" " +"you are "+str(years)+" years old")
