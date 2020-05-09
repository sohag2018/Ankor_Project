print("1 #:---Simple Project with if else------- ")
var1=6
var2=56
var3=int(input("Enter a number:"))
if var3>var2 and var3>var1:
    print("Your number is the biggest one")
elif var3<var2 and var3<var1:
    print("Your number is the smallest one")
else:print("Your number is in between ")

print("2 #:---if else with list------- ")
list =[5,6,8]
print(5 in list)
if 15 in list:
    print("15 is in the list")
else:print("15 is not in the list")

print("3 #:---if else with int input------- ")
print("what is your age?")
age=int(input("Ans:"))
if age<18:
    print("You cant drive")
elif age==18:
    print("We will think about you")
else:print("you are good to drive")

print("4 # Excersise:---making word dictionary------ ")
#create a dictionary and input from the user and return the meanig of the
#word from the dictionary

dic={"pen":"writing stuf",
     "computer":"a machine can compute for you",
     "keyboard":"a part of computer help you to give input",
     "monitor":"A parr of a computer to display"}

word=input("Enter any word from the list(pen, computer,keyboard,monitor)")
if word=="pen":
    print("writing stuf")
elif word=="computer":
    print("a machine can compute for you")
elif word=="keyboard":
    print("a part of computer help you to give input")
elif word=="monitor":
    print("A part of a computer to display")

else: print("Please only enter word from the list")

print("___2nd way to solve (simple)__________________________")
#it will work: just get as a key then print the value accordingly to the key
word1=input("Enter the word:")
dic1={"pen":"writing stuf",
     "computer":"a machine can compute for you",
     "keyboard":"a part of computer help you to give input",
     "monitor":"A part of a computer to display"}
print(dic1[word1])


