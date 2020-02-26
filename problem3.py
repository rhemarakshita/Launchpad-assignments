l=[1,2,3,2,0,65,21,4,2,10]
a=int(input("Enter the Key:"))
b=[]

for i,j in enumerate(l):
	if a==j:
		b.append(i)
print(b)


