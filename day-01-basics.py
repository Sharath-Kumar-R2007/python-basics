str=input("enter the first name:")
print(len(str))
str=input("enter the first name:")
print(str.count("$"))


number=int(input("enter the number:"))
num=number%2
if(num==0):
  print("the number is even")
else:
  print("the number is odd")

  
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
if(num1>num2 and num1>num3):
  print("num1 is greatest:",num1)
elif(num2>num3):
  print("num2 is the greatest:",num3)
else:
  print("num3 is greatest:",num3)
