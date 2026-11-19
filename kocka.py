print("\n1.feladat")
for i in range(40,61,5):
    print(i)

print("2.feladat")
for i in range(200, -1, -40):
    print(i,end=", ")

import random
print("\n3.feladat")
k=[]
for i in range(30):
    j=random.randint(-10,10)

    k.append(j)
valtozo=int(input("Hányasával írjam ki a számokat:"))
if valtozo%j==j-1:
    print()
print(k)
