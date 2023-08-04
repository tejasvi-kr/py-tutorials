friends = ["Kunal", "Shubham", "Shubham", "Shreyas", "Soumya", "Nishita", "Shreya"]
lucky_number = [7,19, 13, 29, 31, 37]
print(friends)
#  FUNCTIONS
lucky2 = lucky_number.copy()
friends.extend(lucky_number) #adds 2 lists together
print(friends)
friends.append("creed") #adds another entry to the friends list
print(friends)
friends.insert(1, "sashwat") #adds value before a given index
print(friends)
friends.remove("Shreya")
print(friends)
friends.clear()
print(friends)
friends.pop() #pops out the last value
print(friends) 
print(friends.index("Shreyas"))
print(friends.count("shubham"))
lucky_number.sort()
print(lucky_number)

