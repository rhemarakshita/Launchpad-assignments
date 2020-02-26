a = input("Enter a String:")
a = a.lower()
x = a.split()
n = x[::-1]
s = " "
s = s.join(n)
s = s.capitalize()
print(s)