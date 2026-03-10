#remove"
collection={1,2,3,4,5,6,7,8}
collection.remove(2)
collection.remove(6)
collection.remove(3)
print(collection)

#clear
collection={1,2,3,4,5,6,7,8}
collection.clear()
print(collection)
print(list(collection))

#Pop
collection={"sharath","naruto","luffy","asta"}
print(collection.pop())
print(collection.pop())

#union
set1 = {1,2,3,4,6,5,7}
set2 = {0,9,8,7,6,5,4}
print(set1)
print(set2)
print(set1.union(set2))      
