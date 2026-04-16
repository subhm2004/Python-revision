# agar bohot sare ek type ke elemts ko store krna h to list use krte hai hum 
friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

print(friends[0])
friends[0] = "Grapes" # Unlike Strings lists are mutable

print(friends[0]) #"Apple"
print(friends[1:4]) # "Orange", 5, 345.06

print(friends[::-1]) # reverse kr dega ye list ko 