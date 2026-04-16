s1 = {1, 45, 6, 78}  
s2 = {7, 8, 1, 78}

# ---- UNION ----
print(s1 | s2)          # ye bhi union dega
print(s1.union(s2))     # same kaam

# ---- INTERSECTION ----
print(s1 & s2)              # common elements
print(s1.intersection(s2))  # same kaam

# ---- DIFFERENCE (s1 - s2) ----
print(s1 - s2)              # s1 me jo hain but s2 me nahi
print(s1.difference(s2))    # same kaam

# ---- DIFFERENCE (s2 - s1) ----
print(s2 - s1)
print(s2.difference(s1))

# ---- SYMMETRIC DIFFERENCE (XOR) ----
# dono sets ke uncommon elements
print(s1 ^ s2)
print(s1.symmetric_difference(s2))

# ---- SUBSET ----
print(s1 <= s2)            # check s1 subset hai ya nahi
print(s1.issubset(s2))     # same

# ---- SUPERSET ----
print(s1 >= s2)            # check s1 superset hai ya nahi
print(s1.issuperset(s2))   # same