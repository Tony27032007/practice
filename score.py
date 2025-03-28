name=input("Enter your name: ")
a=[]
for i in range(0,4):
    score=input("Enter your score/100:")
    a.append(score)
score=int(a[0])
score=int(a[1])         
score=int(a[2])
score=int(a[3])
s=score[0]+score[1]+score[2]+score[3]
s=s/4
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
