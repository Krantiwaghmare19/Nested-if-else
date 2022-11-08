OTP=123456
go=input("enter the facebook link")
if go=="WWW.facebook.com":
    name=input("enter your first name")
    if name>="a" and name<="z":
        print(name)
        name2=input("enter your last name")
        if name2>="a" and name2<="z":
            print(name2)
            year=int(input("enter year"))
            month=int(input("enter the month"))
            date=int(input("enter the date"))
            if year>=1980 and year<=2021 and month>=1 and month<=12 and date>=1 and date<=31:
                print("date is correct")
                gender=input("enter the gender")
                if gender=="male" or gender=="female":
                    print("gender is correct")
                    psd=input("create password")
                    print("sucessfully")
                else:
                    print("incorrect password")
            else:
                print("incorrect birthdate")
        else:
            print("incorrect name")
    else:
        print("incorrect name2")
else:
    print("incorrect link")