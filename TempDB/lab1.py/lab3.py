x = int(input("Enter a value"))
y = int(input("Enter a value"))
z = int(input("Enter a value"))
r1 = (x**2 - y*z)**0.5
r2 = (y**4-z) * (z-x)
final = (r1/r2)
print(final)