#Nested Dictionary
student={
  "name":"sharath",
  "subject":{
    "math":94,
    "phy":93,
    "chem":96,
  }
}

print(student)
print(student["subject"])
print(student["subject"]["chem"])

#keys
print(student.keys())
print(list(student.keys()))
print(len(student.keys()))

#values
print(list(student.values()))

#items
print(student.items())
print(list(student.items()))
pairs=list(student.items())
print(pairs[0])
#print(student["name2"])# error
#print(student.get("name2"))# error
