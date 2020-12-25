# -*- coding: utf-8 -*-
import datetime
program = True
bugun = datetime.datetime.today()


info = {"FirstName":[], "LastName": [], "Age":[], "Year":[] }
while program:
    age= int(input ("Plz enter your age: "))
    if age < 18:
        print("You cant go out because its too dangerous")
        program = False
    else:
        info["Age"].append(age)
        fname= input("Plz enter your name: ")
        info["FirstName"].append(fname)
        lname= input ("Plz enter your surname: ")
        info["LastName"].append(lname)
        year= int(input("Plz enter your birth year: "))
        if bugun.year-age != year:
            print("The age value you entered does not match your birth year.")
            program=False
        else:
            info["Year"].append(year)
            print("Your information: {} ".format(info))
            print("You can go out to the street")
