x = [1,2,3,4,5]
z = len(x)-1
i = 0
while i<z:
    x[i],x[z]=x[z],x[i]
    i += 1
    z -= 1
print(x)   