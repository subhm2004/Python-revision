friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(friends)
friends.append("Shubham")
print(friends)

num_list = [1, 34,62, 2, 6, 11 , 6]

num_list.reverse()
print(num_list) 

print(num_list)
num_list.sort()
print(num_list)

print(num_list.sort()) # None
print(num_list.reverse()) #none


print(num_list.index(11)) # index of element 11
print(num_list.count(6)) # 6 kitni baar aya hai 


num_list.insert(2, 333333) # Insert 333333 such that its index in the list is 3
value = num_list.pop(3) # delete value at index 3 
print(value)
print(num_list)