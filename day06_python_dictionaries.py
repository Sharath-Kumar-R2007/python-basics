# Day 6 – Python Dictionaries Practice
# Topics covered:
# - Creating dictionaries
# - Accessing values using keys
# - Modifying dictionary values
# - Adding new key-value pairs
dict={
  "name":"Sharath Kumar R",
  "subject":["Python","java","c++","c"],
  "topic":("dict","set"),
  "age":18,
  "is_adult":True,
  "marks":96,
  }
print(dict)
print(type(dict))      #type 
print(dict["name"])     #access values
print(dict["subject"])
print(dict["topic"])
print(dict["age"])
print(dict["is_adult"])
print(dict["marks"])
dict["name"]="monkey.D"  # we can change the values (mutable)
dict["surname"]="Luffy"
print(dict)"""
"""
#updating values to dectionary

marks={}

x=int(input("enter the phy:"))
marks.update({"phy":x})

y=int(input("Enter the chem:"))
marks.update({"chem":y})

z=int(input("Enter the math"))
marks.update({"math":z})

print(marks)

#null dictionary
null_dict={}
print(null_dict)

null_dict={}
null_dict["name"]="sharath"
print(null_dict)
