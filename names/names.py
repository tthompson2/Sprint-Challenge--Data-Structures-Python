import time

start_time = time.time()
list_size = 10000

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
names_1.sort()
names_2.sort()
stopping_point = 0

for i in range(list_size):
    #stopping_point = j
    for j in range(list_size):
        if ord((names_1[j]) <= ord(names_2[i])) and names_1[i] != names_2[j]:
            continue
        elif ord((names_1[j]) > ord(names_2[i])):
            break
        else:
            duplicates.append(names_2[j])
            stopping_point = j 

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
