lists = ["ka","ba","ta","sa"]
integers = [1,2,3,4,5,6,7]

lists.extend(integers)
print(lists)
lists.append("guls")
print(lists)
lists.insert(0,"gaga")
print(lists)
lists.insert(1,"abhishek")
print(lists)
lists.insert(2,"krakwagon")
print(lists)
#lists.clear()
#print(lists)
#lists.pop(3)
print(lists)
lists.pop()
print(lists)

print(sum(integers))
print(lists.index("gaga"))
print(lists.count("ka"))
