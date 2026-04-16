marks = {
    "Harsh": 74,
    "Shubham": 56,
    "Rohan": 23,
    0: "karan"
}

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Harry": 99, "Renuka": 100})
print(marks)

print(marks.get("Shubham2"))  # None
# print(marks["Shubham2"])   # Error

# ---- New Methods Added ----

# 1. pop() -> specific key remove karta hai
marks.pop("Rohan")
print("After pop:", marks)

# 2. popitem() -> last inserted item remove karta hai
marks.popitem()
print("After popitem:", marks)

# 3. clear() -> pura dictionary empty kar deta hai
temp = marks.copy()
temp.clear()
print("After clear:", temp)

# 4. copy() -> shallow copy banata hai
new_marks = marks.copy()
print("Copy:", new_marks)

# 5. setdefault() -> key exist nahi hai toh add karega
marks.setdefault("Aman", 50)
print("After setdefault:", marks)

# 6. fromkeys() -> new dictionary create karta hai
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print("Fromkeys:", new_dict)

# 7. len() -> total elements count
print("Length:", len(marks))

# 8. in keyword -> key exist karta hai ya nahi
print("Harsh" in marks)
print("XYZ" in marks)