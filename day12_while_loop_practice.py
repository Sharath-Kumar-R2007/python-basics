#To print 1 to 100
count=1
while count <= 100:
  print(count)
  count = count+1

#TO print 100 to 1
count=100
while count >= 1:
  print(count)
  count -=1
  
#genarate multiplication table for given number
n = int(input("enter the number to multiple :"))
count = 1
while count <= 10:
  table = n*count
  print(n,"x",count,"=",table )
  count = count+1

#to print [1,4,9,16,25,36,49,64,81,100](individualy)
nums = [1,4,9,16,25,36,49,64,81,100]
ind = 0
while ind < len(nums):
  print(nums[ind])
  ind = ind+1
