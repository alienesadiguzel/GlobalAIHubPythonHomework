# -*- coding: utf-8 -*-
import datetime #datetime modülünü kullanarak yaşını yanlış girme ihtimalini kontrol ettim.
program = True #Programın sürekli çalışmasını sağladım.
bugun = datetime.datetime.today() #Bugünün tarihini bu kodla elde ettim.


info = {"FirstName":[], "LastName": [], "Age":[], "Year":[] } #dict yapısını kullarak verileri depoladım.
while program:
    age= int(input ("Plz enter your age: "))
    if age < 18: #İlk başta yaşını kontrol edip direkt olarak girip giremeyeceğini belirledim.
        print("You cant go out because its too dangerous")
        program = False
    else:
        info["Age"].append(age)
        fname= input("Plz enter your name: ")
        info["FirstName"].append(fname)
        lname= input ("Plz enter your surname: ")
        info["LastName"].append(lname)
        year= int(input("Plz enter your birth year: "))
        if bugun.year-age != year: #Burada doğum yılını sorgulayıp yanlış yai girmesini engelledim.
            print("The age value you entered does not match your birth year.")
            program=False
        else:
            info["Year"].append(year)
            print("Your information: {} ".format(info))
            print("You can go out to the street")
