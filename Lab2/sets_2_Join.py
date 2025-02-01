set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"x", "y", "z"}
list1 = ["John", "Elena"]
tuple1 = ("apple", "banana", "cherry")

set = set1.union(set2, list1, tuple1)
print(set)

set = set1 | set2 | set3  #only sets
print(set)



#update
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)




#intersection
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
#or
set3 = set1 & set2                        # 2 or more sets
print(set3)


#intersection_update
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)






#difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
#or
set3 = set1 - set2 #only sets
print(set3)



#difference__update
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)





#symmetric_differnce
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
#or
set3 = set1 ^ set2  #only sets
print(set3)



#symmetric_difference_update
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)