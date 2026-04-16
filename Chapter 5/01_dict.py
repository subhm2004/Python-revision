# Dictionary is a collection of keys-value pairs. 
# lookup bohot fast hota h dictionary me 
#  it cannot contain duplicate keys


d = {} # Empty dictionary
marks = {
    "Hardik": 100,
    "Shubham": 56,
    "Rohan": 23,
    "num_list" : [1,2,3,4,5],
    0 : "malik"
}


print(marks)

print(type(marks))
      
print(marks["Hardik"])


print(marks.items())
print(marks.keys())
print(marks.values())

# loops ka use kr rhe hai dictionary me 
for val in marks.values():
    print(val)

for key in marks.keys():
    print(key)

for key, val in marks.items():
    print(key, "->",val)

