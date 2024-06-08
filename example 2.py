

#celsius= float(input("enter temperature in celsius:"))
#fahrenheit= (celsius*1.8)+32
#print(str(celsius)+" degree celsius is equal to"+ str(fahrenheit)+"degree fahrenheit")



#celsius =int(input("enter the temperature in celsius:"))
#fahrenheit= (1.8*celsius)+ 32
#print("temperature in fahrenheit:",fahrenheit)
#fahrenheit =int(input("enter the temperature in fahrenheit:"))
#celsius= (fahrenheit -32) / 1.8
#print("temperature in celsius:", celsius)



while True:
    print("1.celsius to fahrenheit")
    print("2.fahrenheit to celsius")
    print("3.exit")
    ch =int(input("enter choice:"))
    if ch == 3:
        print("exiting the calculator")
        break           
    if ch == 1:
        C =int(input("enter temperature in celsius:"))
        F =(9/5) *C+32
        print("celsius to fahrenheit is",F)
    elif ch == 2:
        F= int(input("enter temperature in fahrenheit:"))
        C = (F-32) *5/9
        print("fahrenheit to celsius is", C)
    else:
        print("invalid choice")
        comtinue_ch = input("do you want to continue?(yes/no)")
        if continue_ch != "yes":
            print("exiting the temperature conversion")
            break     