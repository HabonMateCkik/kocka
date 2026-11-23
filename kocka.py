print("\n1.feladat")
for i in range(40,61,5):
    print(i)

print("2.feladat")
for i in range(200, -1, -40):
    print(i,end=", ")

import random
print("\n3.feladat")
k=[]
u=30

for i in range(30):
    j=random.randint(-10,10)
    k.append(j)

n=int(input("Hányasával írjam ki a számokat:"))
for i in range(u):
    print(k[i],end=", ")
    if i%n==n-1:
        print()


