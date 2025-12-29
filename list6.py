l = int(input())
h = int(input())
count = 0
for i in range(l,h+1):
    if i%2 != 0:
        count += 1
print(count)