num=[5,4,8,1,9,2]
print(num)
num.sort()
print(num)
num.reverse()
print(num)
print(num[0:4])#slicing
print(max(num))
print(min(num))
num.append(10) #Adding at end
print(num)
num.insert(0,99) # Adding at any specific position
print(num)

num.remove(10) #removing specific data
print(num)
#num.clear()# To clear all data in the list
#print(num)

num2=num.copy()  # To get a replica
print(num2)

num3=[5,3]
num.extend(num3)
print(num)











