#Append same program with different methods
movie=[]
movies=input("enter the 1st movie")
movie.append(movies)
movies=input("Enter 2nd movie")
movie.append(movies)
movies=input("Enter 3rd movie ")
movie.append(movies)
print(movie)

#Append same program with different methods
movies=[]
movies.append(input("Enter the 1st movie:"))
movies.append(input("Enter the 2nd movie:"))
movies.append(input("Enter the 3rd movie:"))
print(movies)

#palindrome
list=[1,2,3,4,5,4,3,2,1]
copy_list=list.copy()
copy_list.reverse()
if(copy_list==list):
  print("Palindrome")
else:
  print("Not palindrome")

#palindrome
str=["A","B","C","B","A"]
copy_str=str.copy()
copy_str.reverse()
if(copy_str==str):
  print("Palindrome")
else:
  print("Not palindrome")
