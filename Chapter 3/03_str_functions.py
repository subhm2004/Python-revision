name = "sHUBHAM"
 
print(len(name)) # 5 ye length dega string ki 


print(name.endswith("HAM")) # kya string end krri hai isse return true or false

print(name.startswith("SH")) # kya string start krri hai isse return true or false (case sensitive hai ye function)


print(name.capitalize()) # first letter ko capital kr dega ye or baki k letters ko small kr dega

string = "Hello ji "
idx = string.find("ll")  # index return krta hai ye 
print(idx)  # Output: 2 

replaced_string = string.replace("l", "p") # dono l ko replace kr dega ye p se
print(replaced_string)  # Output: Heppo ji 


print(string[::-1]) # reverse kr dega ye string ko