name=input("Enter your name: ")
a=[]
x=0
while x<4:
    print("Enter your score for subject ", x+1)
    score=input()
    score=int(score)
    if score<0 or score>100:
        print("You're joking me? Enter a VALID score NOW")
    else:  
       a.append(score)
       a[x]=float(a[x])
       x=x+1
s=a[0]+a[1]+a[2]+a[3]   
s=s/4
print("your name is: ", name)
print("your avg score is: ", s, "%")
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
