print("1 #________________________")
s_from_list=set([1,2,3,4])
print(s_from_list)
print(type(s_from_list))

print("2 #________________________")
s=set()
s.add(1)
s.add(2)
s.add(3)
s.union({1,2,3})    #union-->combined only common element
print(s)
s.remove(3)
print("after removing:",s)

print("3 #---------------------  ")
thisset={1,2,3,4,5}
print(thisset)
thisset.remove(1)
thisset.discard(2) #also used for removing
print("after removing:",thisset)


print("exersize___adding value___________________")
this_set={"1","2","3"}
this_set1={"a","b","c","d"}
this_set.update(this_set1)
print(this_set)
this_set2={"x","y","z"} #{'d', '1', 'a', '2', 'c', 'b', '3'}
print(this_set.union(this_set2)) #{'1', 'a', '2', 'y', '3', 'd', 'z', 'x', 'c', 'b'}