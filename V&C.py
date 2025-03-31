v=["a", "e", "i", "o", "u"]
w=input("Enter a word: ")
n=len(w)
x=0
y=0
for i in range (0,n):
      if w.lower()[i] in v:
            x=x+1
      elif 
            y=y+1
print("Vowels:", x)
print("Consonants:", y)