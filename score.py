name=input("Enter your name: ")
a=[1,2,3,4]
a.clear()
for i in range(0,4):
    score=input("Enter your score/100:")
    a.append(score)
    a[i]=float(a[i])
s=a[0]+a[1]+a[2]+a[3]   
s=s//4
print("your name is: ", name)
print("your avg score is: ", s)
if s>=90:
    print("Excellent ")
elif s>=80 and s<90:
    print("Very Good")
elif s>=70 and s<80:       
    print("Good")
elif s>=60 and s<70:
    print("Satisfactory ")
else:
      print("Needs Improvement ")
