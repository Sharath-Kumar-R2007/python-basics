#To linear search
num = (1,4,9,16,25,36,49,64,81,100)
n = int(input("enter the number to find: "))
ind = 0
found = False

while ind < len(num):
    if num[ind] == n:
        print(n, "is found at index", ind)
        found = True
        break
    ind += 1

if not found:
    print("Number not found")

#break
i=1
while i <= 5:
  print(i)
  if( i == 3):
    break
  i=i+1                                                                           

#Continue
i=1
while i <= 5:
  if( i == 3):
    i=i+1
    continue
  print(i)
  i=i+1

#continue
i=1
while i <= 10:
  if(i%2==0):
     i=i+1
     continue
  else:
     print(i)
  i=i+1                            
