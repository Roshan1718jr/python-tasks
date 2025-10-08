#List
print("list methos")
fruits = ["apple", "banana", "cherry"]
print("Original List:", fruits)
fruits.append("mango")
print("append:", fruits)
fruits.insert(1, "orange")
print("insert:", fruits)
fruits.remove("banana")
print("remove:", fruits)
fruits.pop(2)
print("pop:", fruits)
fruits.sort()
print("sort:", fruits)

#tuple
numbers = (1,2,3,4)
print("Tuple:", numbers)
count_1= numbers.count(1)
print("count number",count_1)

numbers = (10, 20, 30, 20, 40)
print("Tuple:", numbers)
index1 = numbers.index(30)
print("Index of 30:", index1)

#set

colors = {"red", "green", "blue"}
print("show Set:", colors)
colors.add("yellow")
print("add:", colors)
colors.update(["black", "white"])
print("update:", colors)
colors.remove("red")
print("remove:", colors)
colors.discard("blue")
print(" discard:", colors)
colors.clear()
print(" clear:", colors)

#dictionary

student = {"name": "John", "age": 20, "course": "Python"}
print("show Dictionary:", student)
print("Name (using get()):", student.get("name"))
print("All Keys:", student.keys())
print("All Values:", student.values())
student.update({"age": 21, "city": "Chennai"})
print("After update():", student)
student.pop("course")
print("After pop():", student)
