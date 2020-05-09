num1=int(input("Enter 1st Number: "))
sym=input("Enter what you want to do: ")
num2=int(input("Enter 2nd Number: "))

if sym=="+":
    print("Result: ",num1+num2)
elif sym=="-":
    print("Result: ",num1-num2)
elif sym=="*":
    print("Result: ",(num1*num2))
elif sym=="/":
    print("Result: ",(num1/num2))



# name="Amar nam Lal Mia"
# print(len(name))
# print(name[9:12])    # output: Lal
#
# name="Amar nam Lal Mia"
# print(name[0:12:2])    #Aa a a
#
# name="Amar nam Lal Mia"
# print(name[0::2])    # Aa a a i