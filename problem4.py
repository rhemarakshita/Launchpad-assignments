duplicate=[1,1,2,3,4,64,35,93,35,87,4,3,]
def Remove(duplicate):
	c=[]
	for num in duplicate:
		if num not in c:
			c.append(num)
	return c
	
print(Remove(duplicate))			
