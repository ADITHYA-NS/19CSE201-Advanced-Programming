#a list with three elements
# use append and insert
#use pop and remove extra
#pop with index, without index then reverse, then sort, then copy then del

nb=["Adarsh", "Adithya", "Agil Prasanna"]
print("List:",nb)
nb.append("Aishwarya")
print("List after appending:",nb)
nb.insert(0,"Tangella Sri Chandan")
print("List after inserting:", nb)
nb.pop()
print("List after using pop :", nb)
nb.pop(0)
print("List after using pop to delete 1st element:", nb)
nb.remove("Adarsh")
print("List after removing the element'Adarsrh':", nb)
nb.reverse()
print("List on reversing:", nb)
nb.sort()
print("List after sorting:", nb)
c=nb.copy()
print("Copied list:",c)
del nb
print("List", nb)
