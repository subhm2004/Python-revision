s = {1, 5, 32, 54, 5, 5, 5, "Shubham"} # set unordered hote hai 

print(s, type(s))

s.add(566)
print("After add:", s)

s.remove(1) # 1 ko remove kr dega ye set se 
print("After remove:", s)

# ---- New Methods ----

# 1. discard() -> remove jaisa hai, but error nahi deta
s.discard(100)  # element exist nahi hai
print("After discard:", s)

# 2. pop() -> random element remove karta hai
s.pop()
print("After pop:", s)

# 3. clear() -> pura set empty
temp = s.copy()
temp.clear()
print("After clear:", temp)

# 4. copy() -> set copy karta hai
new_set = s.copy()
print("Copy:", new_set)

# 5. union() -> dono sets combine
s2 = {100, 200}
print("Union:", s.union(s2))

# 6. intersection() -> common elements
s3 = {5, 32, 999}
print("Intersection:", s.intersection(s3))

# 7. difference() -> jo elements s me hain par s3 me nahi
print("Difference:", s.difference(s3))

# 8. symmetric_difference() -> uncommon elements
print("Symmetric Difference:", s.symmetric_difference(s3))

# 9. issubset() -> check karta hai subset hai ya nahi
print({5, 32}.issubset(s))

# 10. issuperset() -> check karta hai superset hai ya nahi
print(s.issuperset({5, 32}))

# 11. len() -> total elements
print("Length:", len(s))

# 12. in keyword -> element exist karta hai ya nahi
print(5 in s)
print(999 in s)