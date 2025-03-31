l=[]
n=input("How many number in the list: ")
n=int(n)
if n<2:
      print("list must have more than 2")
int(n)
for i in range (0,n):
      l.append(int(input("Enter a number: ")))

for i in range (0,n):
      l[i]=int(l[i])
      l[i+1]=int(l[i+1])
      if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
print("The second highest number is:", l[n-1])
