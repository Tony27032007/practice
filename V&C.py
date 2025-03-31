v=["a", "e", "i", "o", "u"]
w=input("Enter a word: ")
n=len(w)
i=0
x=0
y=0
while i<n:
      if w[i] in v:
            x=x+1
            i=i+1
      else:
            y=y+1
            i=i+1
print("Vowels:", x)
print("Consonants:", y)