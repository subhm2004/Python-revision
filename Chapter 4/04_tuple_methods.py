a = (1,45,342,3424,False, 45, "Rohan", "Shivam")
print(a)

no = a.count(45)
print(no)

i = a.index(3424)
print(i)

print(len(a))

# 🔹 Membership
print(45 in a)
print("Rohan" in a)

# 🔹 Slicing
print(a[1:5])
print(a[::-1])   # reverse

# 🔹 Concatenation
b = (100, 200)
c = a + b
print(c)

# 🔹 Repetition
print(b * 3)

# 🔹 Iteration
for item in a:
    print(item)

# 🔹 Built-in functions
nums = (5, 2, 9, 1)
print(max(nums))
print(min(nums))
print(sum(nums))

# 🔹 Sorting (returns list)
print(sorted(nums))

# 🔹 Tuple unpacking
t = (10, 20, 30)
x, y, z = t
print(x, y, z)

# 🔹 Nested tuple
nested = (1, (2, 3), (4, 5))
print(nested[1][0]) 