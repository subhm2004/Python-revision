import time

start = time.time()   # start time

n = int(input("Enter the number: "))

for i in range(1, n+1):
    print(i)

end = time.time()     # end time

print("Time taken:", end - start, "seconds")